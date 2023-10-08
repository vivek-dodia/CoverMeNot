from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup
from collections import Counter
import requests
import re
from fpdf import FPDF

# pointing to jinja external template
file_loader = FileSystemLoader(".")
env = Environment(loader=file_loader)
template = env.get_template("template.j2")

# asking for inputs
Your_Name = input("Enter your name: ")
job_title = input("Enter the job title you're applying for: ")
company_name = input("Enter the company name: ")
years_of_experience = input("Enter your years of experience: ")
job_url = input("Enter the job posting URL: ")

# using the job url, scraping the web html
response = requests.get(job_url)
soup = BeautifulSoup(response.text, 'html.parser')

# ssume job_description contains the entire text from the webpage
job_description = soup.get_text(" ", strip=True)

# counting how many times keywords are repeated 
keyword_counter = Counter()

# dictionary for keywords that script will scan through
known_keywords = ["Python", "Networking", "Linux", "AWS", "Ansible", "Docker",
                  "Cisco", "Juniper", "Arista", "Fortinet", "MikroTik", "Calix", "F5 Networks", "Palo Alto Networks", "Ruckus", "Ciena",
                  "AWS", "Azure", "Google Cloud Platform", "IBM Cloud", "Oracle Cloud", "DigitalOcean",
                  "Ansible", "Terraform", "Kubernetes", "Docker", "GitLab CI/CD",
                  "Wireshark", "Nmap", "Nessus", "Burp Suite", "Snort", "OpenVAS", "Metasploit", "Kali Linux", "ZAP", "Splunk",
                  'Network Architecture', 'Routing Protocols', 'VPN Configuration',
                  'Firewall Management', 'Switch Configuration', 'Network Monitoring',
                  'Load Balancing', 'Intrusion Detection Systems',
                  'OSPF', 'BGP', 'VPN', 'IDS',
                  'Cisco IOS', 'Juniper JUNOS', 'Arista EOS', 'Fortinet FortiGate',
                  'MikroTik RouterOS', 'Calix Management', 'Palo Alto Panorama',
                  'Check Point Security Management', 'Ruckus Wireless',
                  'IOS', 'JUNOS', 'EOS',
                  'Cloud Migration', 'Amazon Web Services EC2', 'Azure Virtual Machines',
                  'Google Cloud Platform Compute Engine', 'IBM Cloud Services',
                  'Oracle Cloud Infrastructure', 'DigitalOcean Droplets', 'Alibaba Elastic Compute Service', 
                  'VMware vSphere', 'Rackspace Cloud', 'Salesforce Integration',
                  'AWS', 'EC2', 'VMs', 'GCP', 'IBM', 'ECS',
                  'Infrastructure as Code', 'Ansible Playbooks',
                  'Terraform Scripts','Kubernetes Orchestration',
                  'Docker Containers', 'GitLab Continuous Integration/Continuous Deployment',
                  'IaC', 'CI/CD',
                  'Packet Analysis', 'Network Scanning', 'Vulnerability Assessment',
                  'Web Security', 'Intrusion Prevention', 'OpenVAS Scans', 'Penetration Testing',
                  'Ethical Hacking', 'Log Management',
                  'Wireshark', 'Nmap', 'Nessus', 'Burp', 'Snort', 'OpenVAS', 'Metasploit', 'Kali', 'ZAP', 'Splunk'
                  ]

# count the occurrences of each keyword
for keyword in known_keywords:
    keyword_count = job_description.lower().count(keyword.lower())
    keyword_counter[keyword] = keyword_count

# get the top 5 most frequent keywords
top_keywords = [item[0] for item in keyword_counter.most_common(5)]

# fill in the top 5 repeated keywords in job post in the jinja2 placeholder
custom_variables = {
    "Your_Name": Your_Name,
    "job_title": job_title,
    "company_name": company_name,
    "years_of_experience": years_of_experience,
    "tech_keywords": ", ".join(top_keywords)
}

populated_template = template.render(**custom_variables)

from fpdf import FPDF

# Initialize PDF
pdf = FPDF(format='letter')
pdf.add_page()
pdf.set_font("Times", size=10)


# Add more cells for the other parts of the letter
pdf.multi_cell(0, 8, txt=populated_template) 

# Save the PDF with name .pdf
pdf_output_path = f"C:/Users/Vivek/Documents/CoverLetters/{company_name}_{job_title}.pdf"
pdf.output(name=pdf_output_path, dest="F")

# to make sure this shit is working
print(populated_template)

