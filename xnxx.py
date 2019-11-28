from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)
#blog={
#    'name':'The Frustrated Fucktard',
#    'posts':{}
#}



@app.route('/') #www.mysite.com/, as soon as / encountered, this func executed
#def home():
#    return render_template('index.html')
def home():
    return render_template('index.html')



#@app.route('/post/<int:post_id>')
#def post(post_id):
#    post=blog['posts'].get(post_id)
    #if not post:
        #return render_template('404.jinja2', message=f'A post with id {post_id} was not found')
    
    
#    return render_template('post.Jinja2',post=post)


#@app.route('/post/create', methods=['GET','POST']) #current request at any point of time
#def create():
#    if request.method=='POST':
#        title=request.form.get("title")
#        content=request.form.get("content")
#        post_id=len(blog['posts'])
#        blog['posts'][post_id]={"post_id":post_id, "title":title, 'content': content}
#        return redirect(url_for("post", post_id=post_id))
#    return render_template('create.html')








app.run()

