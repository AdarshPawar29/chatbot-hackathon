import streamlit as st
import os

class Sidebar:

    MODEL_OPTIONS = ["gpt-3.5-turbo", "gpt-4"]
    CHAIN_TYPE_OPTIONS = ["stuff", "map_reduce", "refine", "map-rerank"]
    TEMPERATURE_MIN_VALUE = 0.0
    TEMPERATURE_MAX_VALUE = 1.0
    TEMPERATURE_DEFAULT_VALUE = 0.0
    TEMPERATURE_STEP = 0.01

    @staticmethod
    def about():
        about = st.sidebar.expander("🧠 About Bob ")
        sections = [
            "#### Bob is an AI chatbot for supply chain management that allows users to more easily discuss supply chain concerns and issues linked to the file they upload. 📄",
        ]
        for section in sections:
            about.write(section)

    @staticmethod
    def reset_chat_button():
        if st.button("Reset chat"):
            st.session_state["reset_chat"] = True
        st.session_state.setdefault("reset_chat", False)

    def model_selector(self):
        model = st.selectbox(label="Model", options=self.MODEL_OPTIONS)
        st.session_state["model"] = model

    def chain_type_selector(self):
        chain_type = st.selectbox(label="chain_type", options = self.CHAIN_TYPE_OPTIONS)
        st.session_state["chain_type"] = chain_type

    def temperature_slider(self):
        temperature = st.slider(
            label="Temperature",
            min_value=self.TEMPERATURE_MIN_VALUE,
            max_value=self.TEMPERATURE_MAX_VALUE,
            value=self.TEMPERATURE_DEFAULT_VALUE,
            step=self.TEMPERATURE_STEP,
        )
        st.session_state["temperature"] = temperature
        
    def csv_agent_button(self, uploaded_file):
        st.session_state.setdefault("show_csv_agent", False)
        
        if uploaded_file and os.path.splitext(uploaded_file.name)[1].lower() == ".csv":
            if st.sidebar.button("CSV Agent"):
                st.session_state["show_csv_agent"] = not st.session_state["show_csv_agent"]

    def show_options(self, uploaded_file):
        with st.sidebar.expander("🛠️ Tools", expanded=False):

            self.reset_chat_button()
            self.csv_agent_button(uploaded_file)
            self.model_selector()
            self.chain_type_selector()
            self.temperature_slider()
            st.session_state.setdefault("model", self.MODEL_OPTIONS[0])
            st.session_state.setdefault("chain_type", self.CHAIN_TYPE_OPTIONS[0])
            st.session_state.setdefault("temperature", self.TEMPERATURE_DEFAULT_VALUE)

    