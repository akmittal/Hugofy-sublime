import sublime, sublime_plugin,subprocess,os

class setvars:
	def __init__(self):
		self.platform=sublime.platform()
		if self.platform=="windows":
			self.seprator="\\"
		else:
			self.seprator="/"
		self.settings=sublime.load_settings("Hugofy-settings")
		self.path=self.settings.get("Directory")
		self.sitename=self.settings.get("SiteName")

class HugonewsiteCommand(sublime_plugin.TextCommand):	
	def run(self, edit):
		var=setvars()
		seprator=var.seprator
		settings=var.settings
		path=var.path
		sitename=var.sitename
		process="hugo new site "+path+seprator+sitename
		subprocess.Popen(process)

class HugonewcontentCommand(sublime_plugin.TextCommand):
	def on_done(self,pagename):
		if pagename="":
			sublime.error_message("No filename provided")
		process="hugo new "+pagename
		subprocess.Popen(process)
	def on_change(self,filename):
		pass
	def on_cancel(self):
		sublime.error_message("No filename provided")
	def run(self,edit):
		var=setvars()
		settings=var.settings
		seprator=var.seprator
		path=var.path
		sitename=var.sitename
		f=sublime.active_window().folders()
		os.chdir(path+seprator+sitename)
		sublime.active_window().show_input_panel("Enter file name", "", self.on_done, self.on_change, self.on_cancel)

class HugoversionCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		try:
			out=subprocess.check_output("hugo version",stderr=subprocess.STDOUT,universal_newlines=True)
			sublime.message_dialog(out)
		except:
			sublime.error_message("Hugo not installed")

class HugoserveCommand(sublime_plugin.TextCommand):
	"""Serve Hugo website"""
	def run(self,edit):
		try:
			out=subprocess.check_output("ab version",stderr=subprocess.STDOUT,universal_newlines=True)
			sublime.message_dialog(out)
		except:
			sublime.error_message("Hugo not installed")
		