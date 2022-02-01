import sublime, sublime_plugin
import os.path
import subprocess

class OpenCmdHereCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            subprocess.Popen(os.path.expandvars("%comspec%"), cwd=os.path.dirname(self.view.file_name()))
        except:
            sublime.error_message("Could not open commandline here.")

    def description(self):
        return "Open commandline here"