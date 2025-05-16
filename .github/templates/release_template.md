# Release Notes for {{ version }}

_Date: {{ date }} | Time: {{ time }}_

{% for pr in prs %}
## PR #{{ pr.number }} – {{ pr.title }}
_Created At: {{ pr.created_at }}_

{% if pr.comments %}
{% for comment in pr.comments %}
- {{ comment }}
{% endfor %}
{% else %}
_No comments_
{% endif %}

{% endfor %}
