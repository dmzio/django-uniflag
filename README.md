django-uniflag
==============

inspired by https://github.com/pinax/django-flag

Makes arbitrary flagging of any content easy

Use
============

- Install as usual
- Enable in installed apps and run `syncdb`
- See `conf.py` for possible configuration changes


Include `{% flagform_js %}` tag once on each page, which uses flags - it inludes necessary JS files

Include `{% add_flag_for object user flag_type %}` for each object to be flagged