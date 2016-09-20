---
layout: page
title: Notebooks
permalink: /notebooks/
---

The Colorado Data Science Team maintains a set of notebooks from competitions, tutorials, and other sources. Below is a list
of these resources

<ul>
{% for notebook in site.notebooks %}
<li><a href="{{ notebook.url }}" target="_blank">{{ notebook.title }}</a> available at <a href="https://github.com/codatascience/{{ notebook.repository }}" target="_blank">github.com/CoDataScience/{{ notebook.repository }}</a></li>
{% endfor %}
</ul>

