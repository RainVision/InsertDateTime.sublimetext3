import sublime, sublime_plugin
import datetime

class InsertDateTimeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for r in self.view.sel():
			self.view.erase(edit, r)
			self.view.insert(edit, r.begin(), "%s" %datetime.datetime.now().strftime("%H:%M %Y/%m/%d")+"\n")
