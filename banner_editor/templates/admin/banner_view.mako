<%inherit file="banner_editor:templates/layout.mako"/>

<div class="form-group" style="line-height: 30px">
    <h3>   <label>  Title: </label> </h3>  ${banner.title}
    <h3>    <label>  Image  </label> </h3> <img src='/static/image/${banner.image}' width="300" height=150>
    <h3>  <label>  Status: </label> </h3> ${banner.status} <br>
    <h3>     <label>  Link on resource: </label> </h3> <a href="${banner.url}">${banner.url}</a><br>
    <h3>    <label>  Position: </label> </h3> ${banner.position}
</div>

<br>
<button type="submit" class="btn btn-default" style="background: #FF8C00;" ><a href="${ request.route_url('banner_update',
 _query={'id':banner.id} ) }" style="text-decoration: none; color: #FFFFFF;">Edit banner</a></button>

&ensp; &ensp;

<button type="submit" class="btn btn-default" style="background: #B22222;">
    <a href="${ request.route_url('banner_delete', id=banner.id )}"
       style="text-decoration: none; color: #FFFFFF;">Delete Banner </a></button>

