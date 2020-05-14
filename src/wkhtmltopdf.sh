#!/bin/bash
xvfb-run -a --server-args="-screen 0, 1280x800x24" /bin/wkhtmltopdf -q $*
