law_keywords = {
    "Criminal": ["crime", "accused", "arrested", "charge", "felony", "misdemeanor"],
    "Civil": ["contract", "dispute", "property", "personal injury", "defamation"],
    "Business": ["business", "corporation", "contract", "employment", "merger"],
    "Estate Planning": ["estate", "will", "trust", "probate"],
    "Bankruptcy": ["bankruptcy", "debt", "creditor", "insolvency"],
    "Personal Injury": ["injury", "accident", "negligence", "liability"],
    "Employment": ["job", "employment", "workplace", "discrimination", "wage", "harassment"],
    "Immigration": ["immigration", "visa", "green card", "deportation", "asylum", "citizenship"],
    "Intellectual Property": ["patent", "copyright", "trademark", "infringement"],
    "Tax": ["tax", "IRS", "audit", "deduction"],
    "Environmental": ["environment", "conservation", "pollution", "climate"],
    "Family": ["divorce", "custody", "alimony", "prenuptial", "adoption"],
  }
onboard_questions = {
    "Criminal": (
      "I understand this is a stressful time for you. To best assist you, could you please provide more information?"
      "\n\t1. Could you briefly describe the charges against you?"
      "\n\t2. Where and when were you arrested?"
      "\n\t3. Have you spoken to any law enforcement officers and if so, what was discussed?"
      "\n\t4. Are there any witnesses or evidences that could help your case?"
      "\n\t5. Have you previously consulted with or hired an attorney for this matter?"
      "\n\t6. Are there any impending deadlines or dates of which we should be aware?"
    ),

    "Civil": (
      "I see you're dealing with a civil matter. To help you more effectively, could you please answer the following questions?\n"
      "\n\t1. Could you briefly describe the dispute?"
      "\n\t2. Who are the parties involved in this dispute?"
      "\n\t3. What is your desired outcome from this situation?"
      "\n\t4. Have any legal actions been taken so far?"
      "\n\t5. Are there any impending deadlines or dates of which we should be aware?"
    ),

    "Business": (
        "It appears you need assistance with a business-related issue. To better understand your situation, could you please provide more information?\n"
        "\n\t1. What type of business do you own or are planning to start?"
        "\n\t2. Could you describe the issue or decision you need help with?"
        "\n\t3. Are there any relevant contracts or agreements?"
        "\n\t4. Who are the other parties involved?"
        "\n\t5. What is your desired outcome from this situation?"
        "\n\t6. Are there any impending deadlines or dates of which we should be aware?"
    ),

    "Estate Planning": (
      "It seems you need help with estate planning. To assist you effectively, I need some details.\n"
      "\n\t1. Do you currently have a will or any trusts established?"
      "\n\t2. Could you give a brief overview of your assets?"
      "\n\t3. Do you have a clear idea of how you want your assets distributed after your death?"
      "\n\t4. Are there any specific concerns or requirements you have for your estate plan?"
    ),

    "Bankruptcy": (
      "I understand that facing bankruptcy is a difficult situation. To assist you better, could you please provide more information?\n"
      "\n\t1. Are you filing for bankruptcy as an individual or a business?"
      "\n\t2. Can you provide an overview of your debts and assets?"
      "\n\t3. Have you taken any steps towards bankruptcy filing?"
      "\n\t4. Are there any legal actions currently taken by your creditors?"
    ),

    "Personal Injury": (
      "I'm sorry to hear about your injury. To assist you better, could you please provide more information?\n"
      "\n\t1. Could you briefly describe the accident?"
      "\n\t2. When and where did the accident occur?"
      "\n\t3. What injuries did you sustain?"
      "\n\t4. Have you spoken to any insurance companies and if so, what was discussed?"
      "\n\t5. Have you previously consulted with or hired an attorney for this matter?"
      "\n\t6. Are there any impending deadlines or dates of which we should be aware?"
    ),

    "Employment": (
      "I see you're dealing with an employment-related issue. To help you more effectively, could you please answer the following questions?\n"
      "\n\t1. Could you briefly describe the issue?"
      "\n\t2. Who are the parties involved in this dispute?"
      "\n\t3. What is your desired outcome from this situation?"
      "\n\t4. Have any legal actions been taken so far?"
      "\n\t5. Are there any impending deadlines or dates of which we should be aware?"
    ),

    "Immigration": (
      "It appears you need assistance with an immigration matter. To better serve you, could you please provide more information?\n"
      "\n\t1. Could you describe the immigration issue you're dealing with?"
      "\n\t2. What is your current immigration status?"
      "\n\t3. Have you previously filed any immigration applications or petitions?"
      "\n\t4. Are you facing any deadlines or court dates?"
      "\n\t5. What is your desired outcome in this situation?"
    ),

    "Intellectual Property": (
      "I understand you're seeking help with an intellectual property issue. Can you please provide more information?\n"
      "\n\t1. What type of intellectual property do you need help with?"
      "\n\t2. Could you briefly describe the issue?"
      "\n\t3. Who are the other parties involved?"
      "\n\t4. What is your desired outcome from this situation?"
      "\n\t5. Are there any impending deadlines or dates of which we should be aware?"
    ),

    "Tax": (
      "I see you're dealing with a tax-related issue. To help you more effectively, could you please answer the following questions?\n"
      "\n\t1. Could you briefly describe the issue?"
      "\n\t2. Who are the other parties involved?"
      "\n\t3. What is your desired outcome from this situation?"
      "\n\t4. Have any legal actions been taken so far?"
      "\n\t5. Are there any impending deadlines or dates of which we should be aware?"
    ),

    "Family": (
      "I see you're dealing with a family-related issue. To help you more effectively, could you please answer the following questions?\n"
      "\n\t1. Could you briefly describe the issue?"
      "\n\t2. Who are the other parties involved?"
      "\n\t3. What is your desired outcome from this situation?"
      "\n\t4. Have any legal actions been taken so far?"
      "\n\t5. Are there any impending deadlines or dates of which we should be aware?"
    ),
  }
def identify_law_type(user_input, law_keywords):
  user_input = input(f"\nHow can I assist you today?\n>: ")
  user_input_set = set(user_input.lower().split())
  for law_type, keywords in law_keywords.items():
    while True:
      if user_input_set.intersection(keywords):
        return onboard_questions[law_type], law_type
      else:
        print("I'm sorry, but I couldn't determine the specific type of law your question pertains to. Could you provide more details or try rephrasing your question?")
      break
  return None, None

                  

if __name__ == "__main__":
  None # type: ignore