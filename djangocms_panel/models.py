from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

class Panel(CMSPlugin):
	DEFAULT = 'panel-default'
	PRIMARY = 'panel-primary'
	SUCCESS = 'panel-success'
	INFO = 'panel-info'
	WARNING = 'panel-warning'
	DANGER = 'panel-danger'
	CONTEXT_CHOICES = (
		(DEFAULT, 'Default'),
		(PRIMARY, 'Primary'),
		(SUCCESS, 'Success'),
		(INFO, 'Info'),
		(WARNING, 'Warning'),
		(DANGER, 'Danger'),
	)

	context = models.CharField(max_length=25, choices=CONTEXT_CHOICES, default=DEFAULT)
	title = models.CharField(max_length=100, null=True, blank=True)
	footer = models.CharField(max_length=100, null=True, blank=True)
