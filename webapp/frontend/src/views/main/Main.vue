<template>
  <div>
    <v-navigation-drawer persistent :mini-variant='miniDrawer' v-model='showDrawer' fixed app>
      <v-layout column fill-height>
        <v-list>
          <v-subheader>Main menu</v-subheader>
          <v-list-tile to='/'>
            <v-list-tile-action>
              <v-icon>home</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Go to Homepage</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile to='/account/main/projectview'>
            <v-list-tile-action>
              <v-icon>favorite</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>ProjectView</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile to='/account/main/dashboard'>
            <v-list-tile-action>
              <v-icon>web</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Dashboard</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile to='/account/main/profile/view'>
            <v-list-tile-action>
              <v-icon>person</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Profile</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile to='/account/main/createProject'>
            <v-list-tile-action>
              <v-icon>favorite</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>CreateProject</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile to='/account/main/profile/edit'>
            <v-list-tile-action>
              <v-icon>edit</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Edit Profile</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile to='/account/main/profile/password'>
            <v-list-tile-action>
              <v-icon>vpn_key</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Change Password</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
        <v-divider></v-divider>
        <v-list subheader v-show='hasAdminAccess'>
          <v-subheader>Admin</v-subheader>
          <v-list-tile to='/account/main/admin/users/all'>
            <v-list-tile-action>
              <v-icon>group</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Manage Users</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile to='/account/main/admin/users/create'>
            <v-list-tile-action>
              <v-icon>person_add</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Create User</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>

          <v-list-tile to='/account/main/ProjectView'>
            <v-list-tile-action>
              <v-icon>disabled_visible</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>ProjectView</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>

           <v-list-tile to='/account/main/admin/Projects'>
            <v-list-tile-action>
              <v-icon>disabled_visible</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Project List</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>

          <v-list-tile to='/account/main/voting'>
            <v-list-tile-action>
              <v-icon>how_to_vote</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Create Votinglink</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>

          <v-list-tile to='/account/main/admin/CreateSchool'>
            <v-list-tile-action>
              <v-icon>how_to_vote</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Create School</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>

          <v-list-tile to='/account/main/admin/Schools'>
            <v-list-tile-action>
              <v-icon>how_to_vote</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>School List</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>

          

        </v-list>
        <v-spacer></v-spacer>
        <v-list>
          <v-list-tile @click='logout'>
            <v-list-tile-action>
              <v-icon>close</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Logout</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-divider></v-divider>
          <v-list-tile @click='switchMiniDrawer'>
            <v-list-tile-action>
              <v-icon v-html="miniDrawer ? 'chevron_right' : 'chevron_left'"></v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Collapse</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-layout>
    </v-navigation-drawer>
    <v-toolbar dark color='primary' app>
      <v-toolbar-side-icon @click.stop='switchShowDrawer'></v-toolbar-side-icon>
      <v-toolbar-title v-text='test'></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu bottom left offset-y>
        <v-btn slot='activator' icon>
          <v-icon>more_vert</v-icon>
        </v-btn>
        <v-list>
          <v-list-tile to='/account/main/profile'>
            <v-list-tile-content>
              <v-list-tile-title>Profile</v-list-tile-title>
            </v-list-tile-content>
            <v-list-tile-action>
              <v-icon>person</v-icon>
            </v-list-tile-action>
          </v-list-tile>
          <v-list-tile @click='logout'>
            <v-list-tile-content>
              <v-list-tile-title>Logout</v-list-tile-title>
            </v-list-tile-content>
            <v-list-tile-action>
              <v-icon>close</v-icon>
            </v-list-tile-action>
          </v-list-tile>
        </v-list>
      </v-menu>
    </v-toolbar>
    <v-content>
      <router-view></router-view>
    </v-content>
    <v-footer class='pa-3' fixed app>
      <v-spacer></v-spacer>
      <span>&copy; {{appName}}</span>
    </v-footer>
  </div>
</template>

<script lang='ts'>
import { Vue, Component } from 'vue-property-decorator';
import { appName } from '@/env';
import { readDashboardMiniDrawer, readDashboardShowDrawer, readHasAdminAccess } from '@/store/main/getters';
import { commitSetDashboardShowDrawer, commitSetDashboardMiniDrawer } from '@/store/main/mutations';
import { dispatchUserLogOut } from '@/store/main/actions';
const routeGuardMain = async (to, from, next) => {
  if (to.path === '/account/main') {
    next('/account/main/dashboard');
  } else {
    next();
  }
};
@Component
export default class Main extends Vue {
  public appName = appName;
  public beforeRouteEnter(to, from, next) {
    routeGuardMain(to, from, next);
  }
  public beforeRouteUpdate(to, from, next) {
    routeGuardMain(to, from, next);
  }
  get miniDrawer() {
    return readDashboardMiniDrawer(this.$store);
  }
  get showDrawer() {
    return readDashboardShowDrawer(this.$store);
  }
  set showDrawer(value) {
    commitSetDashboardShowDrawer(this.$store, value);
  }
  public switchShowDrawer() {
    commitSetDashboardShowDrawer(
      this.$store,
      !readDashboardShowDrawer(this.$store),
    );
  }
  public switchMiniDrawer() {
    commitSetDashboardMiniDrawer(
      this.$store,
      !readDashboardMiniDrawer(this.$store),
    );
  }
  public get hasAdminAccess() {
    return readHasAdminAccess(this.$store);
  }
  public async logout() {
    await dispatchUserLogOut(this.$store);
  }
}
</script>