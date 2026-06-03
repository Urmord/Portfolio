import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect(r'z:\Python\jobs.db')

# SQL magic: Group everything by the skill and find the average salary
query = """
SELECT required_skill, AVG(salary) as average_salary, COUNT(*) as number_of_jobs
FROM job_postings
GROUP BY required_skill
ORDER BY average_salary DESC
"""

skill_analysis = pd.read_sql_query(query, conn)
print(skill_analysis)

# Let's visualize it!
skill_analysis.plot(kind='bar', x='required_skill', y='average_salary', color='teal')
plt.title('Average Salary by Skill (Quebec Market Simulator)')
plt.ylabel('Salary ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

conn.close()
