import {Route, Switch} from "react-router-dom";
import React from "react";
import PageNotFound from "../page/notfound/PageNotFound";
import Search from "../page/search/Search";
import Detail from "../page/detail/Detail";

export default function Navigation() {
    return (
        <Switch>
            <Route exact path="/">
                <Search/>
            </Route>
            <Route exact path="/search">
                <Search/>
            </Route>

            <Route exact path="/detail/:id">
                <Detail/>
            </Route>

            <Route>
                <PageNotFound/>
            </Route>
        </Switch>
    );
}
