import streamlit as st
from groq import Groq
import os

# AI client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Personality prompt
system_prompt = """
You are Harshith.

Your texting style:
- affectionate
- stretch words like morninggg or nighttt
- use hearts ❤️
- call her babe or my love
- playful and caring
- use hinglish only for two three words not the whole sentence
- sometimes tease lightly
- keep replies short like real texting
"""

# Floating background words
st.markdown("""
<style>

.bg-text{
  position:fixed;
  top:0;
  left:0;
  width:100%;
  height:100%;
  overflow:hidden;
  pointer-events:none;
  z-index:-1;
}

.bg-text span{
  position:absolute;
  color:white;
  opacity:0.05;
  font-size:28px;
  animation: floatText 20s linear infinite;
}

@keyframes floatText{
  0%{
    transform:translateY(100vh);
  }
  100%{
    transform:translateY(-100vh);
  }
}

.bg-text span:nth-child(1){left:10%; animation-duration:18s;}
.bg-text span:nth-child(2){left:25%; animation-duration:22s;}
.bg-text span:nth-child(3){left:40%; animation-duration:20s;}
.bg-text span:nth-child(4){left:55%; animation-duration:26s;}
.bg-text span:nth-child(5){left:70%; animation-duration:19s;}
.bg-text span:nth-child(6){left:82%; animation-duration:23s;}
.bg-text span:nth-child(7){left:15%; animation-duration:24s;}
.bg-text span:nth-child(8){left:60%; animation-duration:21s;}

</style>

<div class="bg-text">
<span>cutu ji</span>
<span>apricity</span>
<span>babe</span>
<span>baby</span>
<span>madchen</span>
<span>ma gurl</span>
<span>baby girl</span>
<span>baby gurl</span>
</div>

""", unsafe_allow_html=True)

# HH + AS animation → HASH
st.markdown("""
<style>

.anim-box{
    position:relative;
    height:120px;
    font-size:60px;
    font-weight:bold;
    text-align:center;
}

.hh{
    position:absolute;
    left:5%;
    top:20px;
    animation: moveHH 3s forwards;
}

.as{
    position:absolute;
    right:5%;
    top:20px;
    animation: moveAS 3s forwards;
}

@keyframes moveHH{
  0% {left:5%;}
  40% {left:45%;}
  60% {letter-spacing:60px;}
  80% {letter-spacing:60px;}
  100% {opacity:0;}
}

@keyframes moveAS{
  0% {right:5%;}
  50% {right:45%;}
  70% {right:45%;}
  90% {right:45%;}
  100% {opacity:0;}
}

.hash{
  opacity:0;
  animation: showHash 4s forwards;
}

@keyframes showHash{
  0% {opacity:0;}
  80% {opacity:0;}
  100% {opacity:1;}
}

</style>

<div class="anim-box">
  <div class="hh">HH</div>
  <div class="as">AS</div>
</div>

<div class="hash" style="text-align:center;font-size:60px;font-weight:bold;">
HASH ❤️
</div>

""", unsafe_allow_html=True)

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# Chat input
user_input = st.chat_input("Type a message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ]
    )

    reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)