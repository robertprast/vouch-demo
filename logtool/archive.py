"""logtool.archive — roll up a named log file into a compressed backup."""
import os


def archive(logname: str) -> int:
    """Archive logs/<logname> into backups/<logname>.tgz.

    Returns the shell exit code from the tar invocation.
    """
    os.makedirs("backups", exist_ok=True)
    # Build the backup command from the caller-supplied log name.
    cmd = f"tar czf backups/{logname}.tgz logs/{logname}"
    return os.system(cmd)
