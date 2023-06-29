import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle
model = pickle.load(open('body_fat_model.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))
image_path = "https://totalgymdirect.com/total-gym-blog/wp-content/uploads/healthy-lifestyle-commitment-800x533.jpeg"

# Display the image
st.image(image_path, caption='Healthy Lifestyle', use_column_width=True)
st.title("Body Fat Estimator")


age = st.text_input(
    label="Age",
    help=f"Description for input: Age of the person",
    key='age'
)
Weight = st.text_input(
    label="Weight",
    help=f"Description for input: Weight of the person (in kg)",
    key='Weight'
)
Height = st.text_input(
    label="Height",
    help=f"Description for input: Height of the person (in metres)",
    key='Height'
)
chest = st.text_input(
    label="chest",
    help=f"Description for input: chest circumfrence(in cm) of the person",
    key='chest'
)
Neck = st.text_input(
    label="Neck",
    help=f"Description for input: Neck circumfrence(in cm) of the person",
    key='Neck'
)
Abdomen = st.text_input(
    label="Abdomen",
    help=f"Description for input: Abdomen circumfrence of the person(in cm)",
    key='Abdomen'
)
data = [
    ['20-39', '21-39%'],
    ['40-59', '23-33%'],
    ['60-79', '24-35%']
]

# Create a DataFrame from the data
df2 = pd.DataFrame(data, columns=['Age', 'Ideal Body Fat Percentage'])
if st.button("Body Fat"):
    BMI=None
    BMI = float(Weight) / (float(Height) ** 2)
    input_data=([age,BMI,Abdomen,Neck,chest])
    query=np.asarray(input_data,dtype=np.float64)
    reshaped_query=query.reshape(1,-1)
    output=int(abs(model.predict(reshaped_query)[0]))

    st.success("Result")        
    st.title("Body Fat: "+str(output)+"%")
    image_path1="https://fabulousbody.com/wp-content/uploads/2016/03/Ideal-Body-Fat-Percentage-for-Men.png.webp"  
    if output < 13:
        st.image(image_path1, caption="Body Type: Essential Fat", use_column_width=True)
    elif output < 20:
        st.image(image_path1, caption="Body Type: Athletes", use_column_width=True)
    elif output < 24:
        st.image(image_path1, caption="Body Type: Fit", use_column_width=True)
    elif output < 31:
        st.image(image_path1, caption="Body Type: Acceptable", use_column_width=True)
    elif output >= 32:
        st.image(image_path1, caption="Body Type: Obese", use_column_width=True)

        st.markdown("The best way to treat obesity is to eat a healthy, reduced-calorie diet and exercise regularly. To do this you should: eat a balanced, calorie-controlled diet as recommended by your GP or weight loss management health professional (such as a dietitian) join a local weight loss group.")
    

    st.title("Healthy Lifestyle Links")

    links = {
        "Mayo Clinic - Healthy Lifestyle": "https://www.mayoclinic.org/healthy-lifestyle",
        "Harvard Health - Healthy Living": "https://www.health.harvard.edu/topics/healthy-living",
        "World Health Organization (WHO) - Healthy Living": "https://www.who.int/westernpacific/health-topics/healthy-living",
        "National Institute of Health (NIH) - Healthy Living": "https://www.nhlbi.nih.gov/health-topics/education-and-awareness/healthy-living",
        "American Heart Association (AHA) - Healthy Living": "https://www.heart.org/en/healthy-living"
            }
    for name, link in links.items():
        st.write(f"[{name}]({link})")

    st.title("Ideal Body Fat Perecntage by Age")
    st.table(df2)
    
    