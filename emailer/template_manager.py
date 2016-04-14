#!/usr/bin/env python

import jinja2


class TemplateManager():

    def __init__(self, template_dirs):
        '''
            Init a TemplateManager object

            Args:
                - template_dirs (str) - Path to the directory/directories are stored
        '''

        self._template_env = jinja2.Environment(loader=jinja2.FileSystemLoader([template_dirs]))

    def render_template(self, file_name, **kwargs):
        '''
            Render Jinja2 template from file

            Args:
                - file_name (str) - File name of the template to be rendered
                - **kwargs - Ambiguous arguments to be passed to the template
        '''

        template = self._template_env.get_template(file_name)
        return template.render(**kwargs)
