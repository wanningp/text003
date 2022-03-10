#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask 


# In[ ]:


from flask import render_template, request


# In[ ]:


app=Flask(__name__)


# In[ ]:





# In[ ]:


from textblob import TextBlob

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        text=request.form.get("text")
        print(text)
        r=TextBlob(text).sentiment
        return(render_template("index.html", result=r))
    else: 
        return(render_template("index.html", result="2"))


# In[ ]:


if __name__=="__main__":
    app.run()


# In[ ]:




