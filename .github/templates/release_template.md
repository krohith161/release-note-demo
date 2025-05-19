| PR # | Title | Created At (UTC) | Comments |
|------|-------|------------------|----------|
{% for pr in prs -%}
| {{ pr.number }} | {{ pr.title }} | {{ pr.created_at }} | 
{%- if pr.comments|length > 0 -%}
{{ pr.comments | join('<br>') }}
{%- else -%}
_No comments_
{%- endif -%}
|
{% endfor %}