# Sample submission for the Building a Rule-Based AI System in Python project.

---

## Part 1: Initial Project Ideas

### 1. Project Idea 1: Movie Recommendation System
- **Description:**  Build a basic recommendation system using predefined rules.
- **Rule-Based Approach:**  
  - Pre-Defined movies suggestions based on mood or genre 
  - Example: A movie recommendation system that suggests films based on user input like genre preference or mood (e.g., “If the user likes Sci-Fi, recommend Interstellar or Blade Runner”).

### 2. Project Idea 2: Simple Chatbot
- **Description:** Create a simple chatbot using if-elif-else conditions or pattern matching with regular expressions. It could respond to basic user inputs like greetings, FAQs, or simple customer support queries.  
- **Rule-Based Approach:**  
  - Responses are based on keywords such as "hello," "help," or "bye."  
  - Example: A rule-based chatbot for a library that provides information about book availability, opening hours, and borrowing rules.

### 3. Project Idea 3: Financial Advice Assistant
- **Description:** A basic system that provides investment or saving advice based on user inputs.  
- **Rule-Based Approach:**  
  - The system uses rules to recommend certain paths finacially you should take.  
  - Example: If a user says they want low risk, recommend bonds or savings accounts; if they want high returns, suggest stocks or crypto.

### **Chosen Idea:** Movie Recommendation System  
**Justification:** I feel that this would give me a good idea into how the brains behind the computer parse through written sentences to make choices based on input

---

## Part 2: Rules/Logic for the Chosen System

The **Movie Recommendation System** system will follow these rules:

1. **Exact Match Rule:**  
   - **IF** specific words are used for genre and mood → **Recommend the Movies**

2. **Partial Match Rule:**  
   - **IF** If they only give one of the two requested prompts then their will be a seperate sets for the singular choices as well   
     - **Recommend the Movies.**  

3. **No Match Rule:**  
   - **IF** if none of the options are in my sets then a default suggestion of known classics will be displayed

4. **Multiple Inputs**
  - **IF** if the user puts in multiple moods or genre's we will merge the movie selections and strip away duplication
    - **Recommend from multiple sets**


---

## Part 3: Rules/Logic for the Chosen System

Sample input and output: 

Enter preferred genres (e.g., Action, Comedy, Horror, Sci-Fi, Drama or press Enter to skip): action
Enter preferred moods (e.g., Exciting, Funny, Thought-provoking, Dark, Scary, Relaxing, Thrilling or press Enter to skip): funny

We recommend these movies for you: ['The Shawshank Redemption', 'The Dark Knight', 'Inception']

Enter preferred genres (Please use commas for multiple choices)(e.g., Action, Comedy, Horror, Sci-Fi, Drama or press Enter to skip): Drama
Enter preferred moods (Please use commas for multiple choices)(e.g., Exciting, Funny, Thought-provoking, Dark, Scary, Relaxing, Thrilling or press Enter to skip): funny, weird, dark

We recommend these movies for you: ['Se7en', 'Ghostbusters', 'Nightcrawler', 'Forrest Gump', 'The Green Mile', 'Joker', 'The Hangover', 'Dumb and Dumber', 'The Shawshank Redemption']

Enter preferred genres (Please use commas for multiple choices)(e.g., Action, Comedy, Horror, Sci-Fi, Drama or press Enter to skip): 
Enter preferred moods (Please use commas for multiple choices)(e.g., Exciting, Funny, Thought-provoking, Dark, Scary, Relaxing, Thrilling or press Enter to skip): scary, thrilling

We recommend these movies for you: ['Sinister', "Don't Breathe", 'A Quiet Place', 'Alien', 'It', 'The Babadook']

---

## Part 4: Reflection

### Project Overview:
The rule-based movie recommendation system works by categorizing movies based on genres and moods, allowing users to input either or both preferences. The system processes user input in a case-insensitive manner, ensuring flexibility regardless of capitalization. It checks for multiple genres or moods and matches them to predefined lists. If both are provided, it cross-references them for more specific recommendations. If no valid input is given, the system defaults to a general set of popular movies. The final recommendations are compiled into a set to prevent duplicates, ensuring variety in the suggestions.

One of the biggest challenges in designing this system was considering edge cases. Initially, I focused on handling straightforward inputs, but I quickly realized that users might only provide one category (genre or mood) or even multiple options. Ensuring the system didn’t break in these scenarios required carefully structuring the rules. Another challenge was balancing complexity and usability. At times, I considered adding more conditions to make recommendations highly specific, but I had to step back and avoid making the system too complex or restrictive.

Working with AI to assist in the design and coding process was helpful, but also required clear prompting. I had to be specific about the requirements, especially regarding how inputs should be handled and the expected outputs. When the AI’s initial suggestions didn’t fully align with my needs, I refined my requests to focus on areas like case-insensitivity, handling multiple inputs, and default recommendations. This iterative process helped me develop a more effective system while also improving my ability to think critically about the problem.

Overall, this project deepened my understanding of how rule-based AI systems work and the importance of anticipating user behavior when designing them.













