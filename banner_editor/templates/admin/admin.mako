
<div id="range1">
    <div class="outer">
        <div class="middle">
            <div class="inner">
                <div class="login-wr">
                    <div class="modal">
                        %if request.authenticated_userid:
                        Welcome <strong> ${request.authenticated_userid}</strong> ::
                        <a href="${request.route_url('auth_logout')}"> Logout </a>
                        <br>
                        %else:
                        <form action="${request.route_url('auth_login')}" method="post" class="form-inline">

                            <div class="form-group">
                                <label class="form-label">Username</label>
                                <input type="text" name="username" class="form-control" placeholder="Username">
                            </div>
                            <div class="form-group">
                                <label  class="form-label">Password</label>
                                <input type="password" name="password" class="form-control" placeholder="Password">
                            </div>
                            <div class="form-group">
                                <input type="submit" value="Sign in" class="btn btn-default-blue" style="background: #FF8C00">
                            </div>
                        </form>
                        %endif
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>