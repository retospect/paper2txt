from subprocess import Popen, PIPE, STDOUT
import sys


def test_commandline_installed():
    p = Popen(["paper2txt"], stdout=PIPE, stderr=STDOUT)
    out, _ = p.communicate()
    niceout = out.decode("utf-8")
    print(niceout)
    assert "outfile" in niceout
