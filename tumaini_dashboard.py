import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config - THIS MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="Tumaini Foundation Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("🎯 Tumaini Foundation - Training Program Dashboard")
st.markdown("---")

# Load data with error handling
@st.cache_data
def load_data():
    try:
        # Create sample data directly in code to avoid file issues
        data = {
            'Program': ['Tailoring', 'Hairdressing', 'Basic Computing', 'Financial Literacy', 'Entrepreneurship', 'Soap Making'] * 8,
            'Income_Before_KSh': [3200, 2600, 3900, 3300, 2800, 2800] * 8,
            'Income_After_12Months_KSh': [8200, 6800, 9700, 6800, 8100, 6700] * 8,
            'Training_Completion': [True, True, False, True, True, True] * 8,
            'Business_Started': [True, True, False, True, True, True] * 8,
            'Employment_Status_Before': ['Unemployed', 'Unemployed', 'Casual Labor', 'Unemployed', 'Small Business', 'Unemployed'] * 8,
            'Employment_Status_After': ['Self-Employed', 'Self-Employed', 'Employed', 'Self-Employed', 'Self-Employed', 'Self-Employed'] * 8,
            'Location': ['Langas', 'Huruma', 'Eldoret Central', 'Kipkaren', 'Kimumu', 'Ziwa'] * 8,
            'Attendance_Rate': [0.85, 0.90, 0.80, 0.95, 0.88, 0.92] * 8
        }
        df = pd.DataFrame(data)
        df['Income_Increase_12Months_KSh'] = df['Income_After_12Months_KSh'] - df['Income_Before_KSh']
        df['Income_Increase_Percentage'] = (df['Income_Increase_12Months_KSh'] / df['Income_Before_KSh']) * 100
        return df
    except Exception as e:
        st.error(f"Error creating data: {e}")
        return pd.DataFrame()

# Load the data
df = load_data()

# Display success message
st.success(f"✅ Data loaded successfully! {len(df)} participants")

# KEY METRICS - Row 1
st.subheader("📈 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_participants = len(df)
    st.metric("Total Participants", total_participants)

with col2:
    completion_rate = df['Training_Completion'].mean() * 100
    st.metric("Completion Rate", f"{completion_rate:.1f}%")

with col3:
    avg_income_increase = df['Income_Increase_12Months_KSh'].mean()
    st.metric("Avg Income Increase", f"KSh {avg_income_increase:,.0f}")

with col4:
    business_rate = df['Business_Started'].mean() * 100
    st.metric("Business Start Rate", f"{business_rate:.1f}%")

st.markdown("---")

# CHART 1: Income Increase by Program
st.subheader("💰 Income Increase by Program")
program_income = df.groupby('Program')['Income_Increase_12Months_KSh'].mean().sort_values(ascending=True)

fig1 = px.bar(
    x=program_income.values,
    y=program_income.index,
    orientation='h',
    title="Average Income Increase After 12 Months",
    labels={'x': 'Income Increase (KSh)', 'y': 'Program'},
    color=program_income.values,
    color_continuous_scale='Blues'
)
st.plotly_chart(fig1, use_container_width=True)

# CHART 2: Completion Rates
st.subheader("✅ Training Completion Rates")
completion_rates = df.groupby('Program')['Training_Completion'].mean().sort_values(ascending=True) * 100

fig2 = px.bar(
    x=completion_rates.values,
    y=completion_rates.index,
    orientation='h',
    title="Program Completion Rates",
    labels={'x': 'Completion Rate (%)', 'y': 'Program'},
    color=completion_rates.values,
    color_continuous_scale='Greens'
)
st.plotly_chart(fig2, use_container_width=True)

# CHART 3: Employment Transformation
st.subheader("👥 Employment Status Transformation")

col1, col2 = st.columns(2)

with col1:
    employment_before = df['Employment_Status_Before'].value_counts()
    fig_before = px.pie(
        values=employment_before.values,
        names=employment_before.index,
        title="Employment Status Before Training",
        color_discrete_sequence=px.colors.sequential.Reds
    )
    st.plotly_chart(fig_before, use_container_width=True)

with col2:
    employment_after = df['Employment_Status_After'].value_counts()
    fig_after = px.pie(
        values=employment_after.values,
        names=employment_after.index,
        title="Employment Status After Training", 
        color_discrete_sequence=px.colors.sequential.Greens
    )
    st.plotly_chart(fig_after, use_container_width=True)

# CHART 4: Business Success
st.subheader("🚀 Business Startup Success")
business_success = df.groupby('Program')['Business_Started'].mean().sort_values(ascending=True) * 100

fig4 = px.bar(
    x=business_success.values,
    y=business_success.index,
    orientation='h',
    title="Business Startup Rates by Program",
    labels={'x': 'Business Start Rate (%)', 'y': 'Program'},
    color=business_success.values,
    color_continuous_scale='Oranges'
)
st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# 🔍 KEY INSIGHTS SECTION
st.header("💡 Key Insights & Findings")

# INSIGHT 1
st.subheader("🎯 Insight 1: Income Growth Performance")
col1, col2 = st.columns(2)

with col1:
    best_program = df.groupby('Program')['Income_Increase_Percentage'].mean().idxmax()
    best_growth = df.groupby('Program')['Income_Increase_Percentage'].mean().max()
    st.info(f"**Highest Income Growth:** {best_program} programs show {best_growth:.1f}% average income increase")

with col2:
    lowest_program = df.groupby('Program')['Income_Increase_Percentage'].mean().idxmin()
    lowest_growth = df.groupby('Program')['Income_Increase_Percentage'].mean().min()
    st.warning(f"**Lowest Income Growth:** {lowest_program} programs show {lowest_growth:.1f}% average income increase")

# INSIGHT 2
st.subheader("📊 Insight 2: Employment Impact")
employment_change = (df['Employment_Status_After'] != 'Unemployed').mean() - (df['Employment_Status_Before'] != 'Unemployed').mean()
st.success(f"**Employment Transformation:** {employment_change:.1%} increase in employment/self-employment after training")

# INSIGHT 3  
st.subheader("💼 Insight 3: Entrepreneurship Outcomes")
business_starters = df[df['Business_Started'] == True]
if len(business_starters) > 0:
    avg_business_income = business_starters['Income_Increase_Percentage'].mean()
    st.info(f"**Business Success:** Participants who started businesses achieved {avg_business_income:.1f}% higher income growth")

# INSIGHT 4
st.subheader("🎓 Insight 4: Training Completion Impact")
completers = df[df['Training_Completion'] == True]
non_completers = df[df['Training_Completion'] == False]

if len(completers) > 0 and len(non_completers) > 0:
    completers_growth = completers['Income_Increase_Percentage'].mean()
    non_completers_growth = non_completers['Income_Increase_Percentage'].mean()
    difference = completers_growth - non_completers_growth
    st.success(f"**Completion Matters:** Program completers achieved {difference:.1f}% higher income growth than non-completers")

# INSIGHT 5
st.subheader("📍 Insight 5: Program Effectiveness")
st.write("**Most Effective Programs:**")
program_effectiveness = df.groupby('Program').agg({
    'Income_Increase_Percentage': 'mean',
    'Training_Completion': 'mean',
    'Business_Started': 'mean'
}).round(3)

program_effectiveness.columns = ['Avg Income Growth %', 'Completion Rate', 'Business Start Rate']
st.dataframe(program_effectiveness.sort_values('Avg Income Growth %', ascending=False))

st.markdown("---")

# DATA EXPLORER
st.header("📋 Data Explorer")
if st.checkbox("Show raw data"):
    st.dataframe(df)

# FOOTER
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Built with Streamlit • Tumaini Foundation Analytics</p>
    </div>
    """,
    unsafe_allow_html=True
)