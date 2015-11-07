import sublime, sublime_plugin,subprocess,os

class setvars:
	def __init__(self):
		self.platform=sublime.platform()
		if self.platform=="windows":
			self.seprator="\\"
		else:
			self.seprator="/"
		self.settings=sublime.load_settings("hugofy-settings")
		self.path=self.settings.get("Directory")
		
		self.sitename=self.settings.get("sitename")	
		if not os.path.exists(self.path+self.seprator+self.sitename):
			 os.makedirs(self.path+self.seprator+self.sitename)
		os.chdir(self.path+self.seprator+self.sitename)

class HugonewsiteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		var=setvars()
		seprator=var.seprator
		path=var.path
		sitename=var.sitename
		process="hugo new site "+path+seprator+sitename
		subprocess.Popen(process)

class HugonewcontentCommand(sublime_plugin.TextCommand):
	def on_done(self,pagename):
		if not pagename:
			sublime.error_message("No filename provided")
		process="hugo new "+pagename
		subprocess.Popen(process)
		sublime.active_window().open_file(self.path+self.seprator+self.sitename+self.seprator+"content"+self.seprator+pagename)
	def on_change(self,filename):
		pass
	def on_cancel(self):
		sublime.error_message("No filename provided")
	def run(self,edit):
		var=setvars()
		self.seprator=var.seprator
		self.path=var.path
		self.sitename=var.sitename
		print(self.path,self.seprator,self.sitename)
		
		sublime.active_window().show_input_panel("Enter file name", "", self.on_done, self.on_change, self.on_cancel)

class HugoversionCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		try:
			out=subprocess.check_output("hugo version",stderr=subprocess.STDOUT,universal_newlines=True)
			sublime.message_dialog(out)
		except:
			sublime.error_message("Hugo not installed")

class HugoserverCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		try:
			out=subprocess.Popen("hugo server --buildDrafts --watch",stderr=subprocess.STDOUT,universal_newlines=True)
			sublime.status_message(out)
		except:
			sublime.error_message("Hugo not installed")


class HugobuildCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		try:
			out=subprocess.Popen("hugo --buildDrafts",stdout=subprocess.PIPE)
			#print(out.communicate()[0].decode('utf-8'))
			sublime.message_dialog(out.communicate()[0].decode('utf-8'))
		except:
			sublime.error_message("Hugo not installed")