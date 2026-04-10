if st.button('Predict Churn'):

    # input data
    input_data = {
        'gender': gender,
        'SeniorCitizen': 1 if senior_citizen == 'Yes' else 0,
        'tenure': tenure,
        'MonthlyCharges': monthly_charges
    }

    input_df = pd.DataFrame([input_data])

    # one-hot encoding
    input_encoded = pd.get_dummies(input_df)

    # match training columns
    for col in model_columns:
        if col not in input_encoded.columns:
            input_encoded[col] = 0

    input_encoded = input_encoded[model_columns]

    # prediction
    prediction = model.predict(input_encoded)[0]
    probability = model.predict_proba(input_encoded)[0]
    churn_prob = probability[1] * 100

    # -------------------------
    # OUTPUT DASHBOARD
    # -------------------------
    st.subheader("📊 Risk Analysis Dashboard")

    st.metric("Churn Probability", f"{churn_prob:.1f}%")

    if prediction == 1:
        st.error("⚠️ High Risk Customer")

        st.warning("📌 Business Action Recommendations")
        st.write("""
        - Offer discount or loyalty bonus  
        - Contact customer for feedback  
        - Provide priority support  
        - Run retention campaign immediately  
        """)

    else:
        st.success("✅ Low Risk Customer")

        st.info("📌 Growth Strategy Recommendations")
        st.write("""
        - Upsell premium services  
        - Offer referral rewards  
        - Improve engagement programs  
        - Strengthen long-term loyalty  
        """)

    # Gauge chart
    st.plotly_chart(create_gauge(churn_prob / 100))
