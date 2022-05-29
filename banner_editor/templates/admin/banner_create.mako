<%inherit file="banner_editor:templates/layout.mako"/>

<h1>Create Banner </h1>

<FORM action="${request.route_url('banner_create')}" method="post" class="form">

            % for error in form.title.errors:
                <div class="error">{{ error }}</div>
            % endfor

            <div class="form-group" style="line-height: 30px">
                <label>  Title: </label>  ${form.title} <br>
                <label>  Image  </label>  ${form.image} <br>
                <label>  Status: </label>  ${form.status} <br>
                <label>  Link on resource: </label>  ${form.url} <br>
                <label>  Position: </label>  ${form.position}
            </div>

    <div class="form-group">
            <button type="submit" class="btn btn-default" style="background: #FF8C00">Create</button>
    </div>
</FORM>

<br>
<button type="submit" class="btn btn-default" style="background: #000000"> <a href="${request.route_url('home')}" style='text-decoration: none;
 color: #FFFFFF;'>Home page </a></button>

