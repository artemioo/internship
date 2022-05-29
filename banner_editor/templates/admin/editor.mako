<%inherit file="banner_editor:templates/layout.mako"/>

    %if request.authenticated_userid:
    Welcome <strong> ${request.authenticated_userid}</strong> ::
    <a href="${request.route_url('auth_logout')}"> Logout </a>
    <br>
    % else:
    <form action="${request.route_url('auth_login')}" method="post" class="form-inline">

        <div class="form-group">
            <input type="text" name="username" class="form-control" placeholder="Username">
        </div>
        <div class="form-group">
            <input type="password" name="password" class="form-control" placeholder="Password">
        </div>
        <div class="form-group">
            <input type="submit" value="Sign in" class="btn btn-default-blue" style="background: #FF8C00">
        </div>
    </form>
    %endif
    <br>
    <form action="${request.route_url('banner_create')}">
        <button> Create Banner </button>
    </form>

<br>

    <form action="${request.route_url('editor')}">
        <h4> Filter by status </h4>
        <input type="checkbox" name="filter_type" value="Disabled"> Disabled
        <input type="checkbox" name="filter_type" value="Enabled"> Enabled <br>
        <button type="submit"> Drop Filter </button>
        <button type="submit"> Show </button>

    </form>


    %if paginator.items:
    <table>
        <col width="190" >
        <col width="130">
        <col width="530">
        <col width="150">
        <col width="100">
        <tr>

        <th> <a href="${ request.route_url('editor', _query={'sort': 'title', 'size': '3', 'dir': sort_asc_desc, 'filter_type': filter_type}) }" >Title</a></th> &ensp; &ensp;
        <th><a href="${ request.route_url('editor', _query={'sort': 'status', 'size': '3', 'dir': sort_asc_desc, 'filter_type': filter_type}) }" >Status</a></th>
        <th>Image & URL  </th>
        <th><a href="${ request.route_url('editor', _query={'sort': 'position', 'size': '3', 'dir': sort_asc_desc, 'filter_type': filter_type}) }" >Position</a></th>
        <th> Action </th>
    </tr>
    %for banner in paginator.items:
    <tr>
        <td> <strong> ${banner.title} </strong> </td>
        <td>${banner.status.value}</td>
        <td><a href="${banner.url}"><img src="/static/image/${banner.image}" width="300" height='200'> </a></td>

        <td>${banner.position} </td>
        <td>

            <a href="${ request.route_url('banner_update', _query={'id':banner.id})}" style="text-decoration: none; color: #FFFFFF;">
                <img class="logo img-responsive" src="${request.static_url('banner_editor:static/office-material.png') }" alt="pen_edit"  width="35" height="35"></a>

            &ensp;
            <a href="${ request.route_url('banner_delete', id=banner.id )}"
               style="text-decoration: none; color: #FFFFFF;">
                <img class="logo img-responsive" src="${request.static_url('banner_editor:static/remove.png') }" alt="pen_delete"  width="35" height="35"></a>
        </td>
    </tr>
    %endfor
</table>

${paginator.pager() | n}
%endif
