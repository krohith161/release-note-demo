# Release Notes for {{ version }}

_Date: {{ date }}_
_Time: {{ time }}_

{% for pr in prs %}
## PR #{{ pr.number }} – {{ pr.title }}

{% if pr.comments %}
{% for comment in pr.comments %}
- {{ comment }}
{% endfor %}
{% else %}
_No comments_
{% endif %}

{% endfor %}
