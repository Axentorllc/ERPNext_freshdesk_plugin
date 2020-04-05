# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "freshdesk_plugin"
app_title = "Freshdesk Plugin"
app_publisher = "Axentor LLC"
app_description = "Plugin for FreshDesk & FreshChat"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "opensource@axentor.net"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/freshdesk_plugin/css/freshdesk_plugin.css"
app_include_js = "/assets/freshdesk_plugin/js/freshdesk_plugin.js"
# app_include_js = "https://euc-widget.freshworks.com/widgets/77000000474.js"

# include js, css files in header of web template
# web_include_css = "/assets/freshdesk_plugin/css/freshdesk_plugin.css"
# web_include_js = "/assets/freshdesk_plugin/js/freshdesk_plugin.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "freshdesk_plugin.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "freshdesk_plugin.install.before_install"
# after_install = "freshdesk_plugin.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "freshdesk_plugin.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"freshdesk_plugin.tasks.all"
# 	],
# 	"daily": [
# 		"freshdesk_plugin.tasks.daily"
# 	],
# 	"hourly": [
# 		"freshdesk_plugin.tasks.hourly"
# 	],
# 	"weekly": [
# 		"freshdesk_plugin.tasks.weekly"
# 	]
# 	"monthly": [
# 		"freshdesk_plugin.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "freshdesk_plugin.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "freshdesk_plugin.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "freshdesk_plugin.task.get_dashboard_data"
# }

