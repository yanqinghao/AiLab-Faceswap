import io
import os
import re

from nbconvert.exporters.script import ScriptExporter  # pylint: disable=import-error
from notebook.utils import to_api_path  # pylint: disable=import-error


def fix_cli(script):
    cli_regex = r"(get_ipython\(\).system\(((?P<quote>[\'\"]).*?(?P=quote))\))"
    var_regex = r"\{(.+?)\}"

    def _repl(match):
        cli_string = match.group(2)
        groups = re.findall(var_regex, cli_string)
        cli_string = re.sub(var_regex, "{}", cli_string)
        if groups:
            cli_string += ".format({})".format(", ".join(groups))
        cli_string = "import os; os.system({})".format(cli_string)
        return cli_string

    return re.sub(cli_regex, _repl, script)


def script_post_save(model, os_path, contents_manager, **kwargs):
    """Save a copy of notebook to the corresponding language source script.
    For example, when you save a `foo.ipynb` file, a corresponding `foo.py`
    python script will also be saved in the same directory.
    However, existing config files I found online (including the one written in
    the official documentation), will also create an `Untitile.txt` file when
    you create a new notebook, even if you have not pressed the "save" button.
    This is annoying because we usually will rename the notebook with a more
    meaningful name later, and now we have to rename the generated script file,
    too!
    Therefore we make a change here to filter out the newly created notebooks
    by checking their names. For a notebook which has not been given a name,
    i.e., its name is `Untitled.*`, the corresponding source script will not be
    saved. Note that the behavior also applies even if you manually save an
    "Untitled" notebook. The rationale is that we usually do not want to save
    scripts with the useless "Untitled" names.
    """
    # only process for notebooks
    if model["type"] != "notebook":
        return

    script_exporter = ScriptExporter(parent=contents_manager)
    base, __ = os.path.splitext(os_path)

    # do nothing if the notebook name ends with `Untitled[0-9]*`
    regex = re.compile(r"Untitled[0-9]*$")
    if regex.search(base):
        return

    script, resources = script_exporter.from_filename(os_path)
    script_fname = base + resources.get("output_extension", ".txt")

    log = contents_manager.log
    log.info(
        "Saving script at /%s", to_api_path(script_fname, contents_manager.root_dir)
    )

    script = fix_cli(script)

    with io.open(script_fname, "w", encoding="utf-8") as f:
        f.write(script)


c.FileContentsManager.post_save_hook = (
    script_post_save
)  # pylint: disable=undefined-variable
