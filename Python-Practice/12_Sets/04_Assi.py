python = {"Python", "SQL", "Git", "Django"}
web = {"Html", "css", "javascript", "React", "Git"}
# find and print
# common skill all unique skills pyhton only skills web-only-skills non common skills

common = python & web 
all_skills = python |web
python_only = python - web
web_only = web -python
non_common = python ^ web

print("Common:", common)
print("All:", all_skills)
print("Python only:", python_only)
print("Web only:", web_only)
print("Non-common:", non_common)
