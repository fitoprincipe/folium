# -*- coding: utf-8 -*-

"""
ScrollZoomToggler plugin
------------------------

Adds a button to enable/disable zoom scrolling.

"""

from __future__ import (absolute_import, division, print_function)

from branca.element import MacroElement

from jinja2 import Template


class ScrollZoomToggler(MacroElement):
    def __init__(self):
        """Creates a button for enabling/disabling scroll on the Map."""
        super(ScrollZoomToggler, self).__init__()
        self._name = 'ScrollZoomToggler'

        self._template = Template("""
            {% macro header(this,kwargs) %}
                <style>
                    #{{this.get_name()}} {
                        position:absolute;
                        width:35px;
                        bottom:10px;
                        height:35px;
                        left:10px;
                        background-color:#fff;
                        text-align:center;
                        line-height:35px;
                        vertical-align: middle;
                        }
                </style>
            {% endmacro %}

            {% macro html(this,kwargs) %}
            <img id="{{this.get_name()}}" alt="scroll"
                 src="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/png/512/arrow-move.png"
                 style="z-index: 999999"
                 onclick="{{this._parent.get_name()}}.toggleScroll()">
            </img>
            {% endmacro %}

            {% macro script(this,kwargs) %}
                    {{this._parent.get_name()}}.scrollEnabled = true;

                    {{this._parent.get_name()}}.toggleScroll = function() {
                        if (this.scrollEnabled) {
                            this.scrollEnabled = false;
                            this.scrollWheelZoom.disable();
                            }
                        else {
                            this.scrollEnabled = true;
                            this.scrollWheelZoom.enable();
                            }
                        };

                    {{this._parent.get_name()}}.toggleScroll();
            {% endmacro %}
            """)
