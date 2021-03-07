from cefpython3 import cefpython as cef
import platform
import sys
def main():
    check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    cef.CreateBrowserSync(url="https://mope.io/",
                          window_title="Chrome in Python")
    cef.MessageLoop()
    cef.Shutdown()
def check_versions():
    assert cef.__version__ >= "55.3", "CEF Python v55.3+ required to run this"
if __name__ == '__main__':
    main()
