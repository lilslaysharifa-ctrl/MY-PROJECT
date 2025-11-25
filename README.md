📊 Tumaini Foundation Dashboard
A comprehensive Streamlit dashboard for monitoring and analyzing the impact of Tumaini Foundation's vocational training programs in Kenya.

https://via.placeholder.com/800x400/4CAF50/white?text=Tumaini+Foundation+Dashboard

🌟 Overview
This interactive dashboard provides real-time insights into the performance and outcomes of various vocational training programs offered by Tumaini Foundation. Track key metrics, visualize program effectiveness, and make data-driven decisions to improve community impact.

🚀 Features
📈 Key Metrics
Total Participants tracking

Training Completion Rates

Average Income Increase (KSh)

Business Startup Success Rates

📊 Visual Analytics
Income Growth Analysis by program

Employment Status Transformation (before vs after)

Business Startup Success rates

Program Completion performance

💡 Smart Insights
Program effectiveness ranking

Income growth comparisons

Employment impact analysis

Training completion benefits

🛠 Installation
Prerequisites
Python 3.8 or higher

pip (Python package manager)

Step-by-Step Setup
Clone the repository

bash
git clone https://github.com/lilslaysharifa-ctrl/MY-PROJECT.git
cd MY-PROJECT
Create a virtual environment (recommended)

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install required packages

bash
pip install streamlit pandas plotly
Run the application

bash
streamlit run app.py
View the dashboard

The app will automatically open in your default browser

If not, navigate to http://localhost:8501

📁 Project Structure
text
MY-PROJECT/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── assets/               # Additional resources (if any)
    ├── images/
    └── data/
🎯 Usage
Navigating the Dashboard
Key Metrics Section

View at-a-glance performance indicators

Monitor overall program success

Income Analysis

Compare income increases across programs

Identify highest-performing training courses

Employment Transformation

Track employment status changes

Visualize program impact on livelihoods

Business Success Metrics

Monitor entrepreneurship outcomes

Analyze business startup rates

Data Exploration
Toggle "Show raw data" checkbox to view underlying dataset

Interactive charts for detailed analysis

Export-ready visualizations

📊 Data Schema
The dashboard uses the following data structure:

Column	Description	Type
Program	Training program name	String
Income_Before_KSh	Pre-training income	Integer
Income_After_12Months_KSh	Post-training income	Integer
Training_Completion	Program completion status	Boolean
Business_Started	Business initiation	Boolean
Employment_Status_Before	Pre-training employment	String
Employment_Status_After	Post-training employment	String
Location	Participant location	String
Attendance_Rate	Training attendance	Float
🔧 Customization
Adding New Programs
Modify the sample data in the load_data() function:

python
data = {
    'Program': ['New Program', ...],
    'Income_Before_KSh': [values...],
    # ... other columns
}
Modifying Visualizations
Update chart colors in color_continuous_scale parameters

Adjust metrics calculations in aggregation functions

Customize layout in Streamlit components

🌍 Impact Metrics
The dashboard helps track:

✅ Economic empowerment through income growth

✅ Skills development completion rates

✅ Entrepreneurship and job creation

✅ Community development indicators

🤝 Contributing
We welcome contributions to enhance the dashboard:

Fork the repository

Create a feature branch (git checkout -b feature/improvement)

Commit changes (git commit -am 'Add new feature')

Push to branch (git push origin feature/improvement)

Create a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🆘 Support
For technical support or questions:

Create an issue on GitHub

Contact the development team

Check documentation updates

📞 Contact
Tumaini Foundation
📧 Email: info@tumainifoundation.org
🌐 Website: www.tumainifoundation.org
📍 Location: Eldoret, Kenya

Development Team
👩‍💻 Developer: lilslaysharifa-ctrl
🐛 Report Issues: GitHub Issues

<div align="center">
Built with ❤️ for Tumaini Foundation's mission of empowering communities through education and skills development

Making Data-Driven Decisions for Social Impact

</div>
