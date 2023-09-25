# CoverMeNot 📝 

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
     
We're leveraging the power of **BeautifulSoup** 🍲 to scrape the job deets off that URL you so generously provided. Spice it up with 🌶️:

- You'll spot a `known_keywords` 📝 list in the script. It's chock-full of industry lingo 🤓.
- **Go nuts** 🥜 and tweak this list with any other industry-specific buzzwords 🐝.
- Post-scrape, BeautifulSoup and Python's `Counter` 📊 team up to tally the most frequently dropped terms from our `known_keywords`.
- These hot terms 🌶️ are then magically ✨ placed into the template.

So there you have it, a **customized cover letter** that's recruiter-friendly 🤝. Mind = blown 🤯.
Bam! You're now prepped to wow some hiring peeps without even breaking a sweat. 👌

--------------------------------------

## How CoverMeNot Works Behind the Curtain 🎭

Wondering what makes this magic trick tick? Look no further:

### Step 1: Setting Up The Stage 🎬
- We kick things off with the **Jinja2** template engine. The template is an external file you can jazz up whenever you feel like it.

### Step 2: The Interrogation Room 🕵️
- Basic info like your name, the job title, and the company is needed. You know the drill.

### Step 3: Web Scraping Like a Boss 🕸️
- We scrape the job posting using **BeautifulSoup**. Only the good stuff (text) comes with us.

### Step 4: Word Hunt 🎯
- We count relevant job and skill keywords using Python's **Counter** class.

### Step 5: Personalization, Baby! 💅
- The top 5 frequent keywords from the job posting are inserted into the **Jinja2** template. Customization at its finest.

### Step 6: PDF Magic 📄
- With **FPDF**, we transform your decked-out cover letter into a PDF. Retro, but effective.

### Step 7: Save the Day 🏆
- The PDF is saved in your chosen folder. Make sure to update this folder path to suit your needs!

### Step 8: Sanity Check 🧠
- We print out the populated template to the console, just to show it's not all smoke and mirrors.

### 🌟 Extra Goodies 🌟
- You can add or remove placeholders in the Jinja2 template to better match your style. The world is your oyster.
  
- You can also modify the Jinja2 template any way you like. Go wild! 🎉

### 🌈 Future Updates 🌈
- Planning to introduce multiple templates based on different industries.
  
- Considering adding an OpenAI API key placeholder to generate on-the-fly templates based on job descriptions.

- Tinkering with the idea of creating a Terminal User Interface because let's face it, GUIs are so 2000-and-late. 🤓

### 🤝 Contributing 🤝
Hey, I might get busy with other tech wizardry or simply get too lazy. This project is open-source so feel free to contribute and make it even cooler than it already is. 🚀



