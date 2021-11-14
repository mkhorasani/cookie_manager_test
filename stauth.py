import streamlit as st
import streamlit_authenticator as stauth

names = ['John','Rebecca']
usernames = ['js','rb']
passwords = ['12','45']

st.title('Test')

hashed_passwords = stauth.hasher(passwords).generate()

#authenticator = stauth.authenticate(names,usernames,hashed_passwords,'stauths','12d3',cookie_expiry_days=0)
#name, authentication_status = authenticator.login('Logins','sidebar')

#if authentication_status:
#    st.write('Welcome *%s*' % (name))
#elif authentication_status == False:
#    st.error('Username/password is incorrect')
#elif authentication_status == None:
#    st.warning('Please enter your username and password')
