# CoverMeNot

Ever thought, "Wow, I can't wait to write another cover letter"? Yeah, me neither. 🙄 So I whipped up this Python + Jinja lovechild to pump out cover letters like they're going out of style. 🚀 Tailor it to your own gig

### How to Use CoverMeNot 📝

1. **Clone the Repo**: 
   - Run `git clone https://github.com/vivek-dodia/CoverMeNot.git` to get all that juicy source code on your local machine.

2. **Install Requirements**: 
   - Navigate to the project folder like a pro and hit `pip install -r requirements.txt`.

3. **Run the Script**: 
   - Type `python engine.py` to get the party started. 🚀

4. **Answer Prompts**: 
   - It's quiz time! The script will prompt you for some deets. All part of the customization process, you know? 😉

5. **Generate PDF**: 
   - Chill for a sec. Your tailor-made cover letter is getting PDF-ified. 📄

6. **Check Output**: 
   - Head over to the output folder (or wherever you told it to save) and marvel at your brand new cover letter.

Bam! You're now prepped to wow some hiring peeps without even breaking a sweat. 👌

--------------------------------------

## How CoverMeNot Works Behind the Curtain 🎭

So you're curious about what's under the hood? Let's break it down:

### Step 1: Setting Up The Stage 🎬
- We're using the **Jinja2** template engine to customize your cover letter. The template lives externally, so you can tweak it anytime.
  
### Step 2: The Interrogation Room 🕵️
- You'll be prompted to provide some basic info: Your name, the job title, the company, and so on. Easy-peasy.
  
### Step 3: Web Scraping Like a Boss 🕸️
- Using **BeautifulSoup**, we scrape the job posting page you provide. We don't care about images, just the text.

### Step 4: Word Hunt 🎯
- Keywords related to job roles, skills, and tech are identified and counted. This uses the **Counter** class from Python's standard library.

### Step 5: Personalization, Baby! 💅
- The script picks up the top 5 most frequent keywords from the job description. These keywords are then fed to the **Jinja2** template to make your cover letter not suck.

### Step 6: PDF Magic 📄
- Using **FPDF**, we convert your customized cover letter into a PDF. Because people still love the '90s.

### Step 7: Save the Day 🏆
- Finally, the PDF gets saved in your chosen folder. Just like that, you're one step closer to getting your dream job (or any job, we're not picky).

### Step 8: Sanity Check 🧠
- To be sure it's not all smoke and mirrors, the populated template is printed to the console.

And there you have it! You're basically stealing a job without actually writing a cover letter. 🙌


