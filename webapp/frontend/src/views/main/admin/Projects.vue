<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title> Projekte verwalten</v-toolbar-title>
      <v-spacer></v-spacer>
      
    </v-toolbar>
    <v-data-table :headers='headers' :items='users'>
      <template slot='items' slot-scope='props'>
        <td>{{ props.item.name }}</td>
        <td>{{ props.item.email }}</td>
        <td>{{ props.item.full_name }}</td>
        <td><v-icon v-if='props.item.is_active'>checkmark</v-icon></td>
        <td><v-icon v-if='props.item.is_superuser'>checkmark</v-icon></td>
        <td><v-icon v-if='props.item.is_teacher'>checkmark</v-icon></td>
        <td class='justify-center layout px-0'>
          <v-tooltip top>
            <span>Edit</span>
            <v-btn
              slot='activator'
              flat
              :to="{
                name: 'main-admin-users-edit',
                params: { id: props.item.id },
              }"
            >
              <v-icon>edit</v-icon>
            </v-btn>
          </v-tooltip>
        </td>
      </template>
    </v-data-table>
  </div>
</template>

<script lang='ts'>
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { IUserProfile } from '@/interfaces';
import { readAdminUsers } from '@/store/admin/getters';
import { dispatchGetProjectData } from '@/store/admin/actions';

@Component
export default class AdminUsers extends Vue {
  public headers = [
    {
      text: 'Name',
      sortable: true,
      value: 'project_name',
      align: 'left',
    },
    {
      text: 'Group',
      sortable: true,
      value: 'group_name',
      align: 'left',
    },
    {
      text: 'Description',
      sortable: false,
      value: 'description',
      align: 'left',
    },
    {
      text: 'Votes',
      sortable: true,
      value: 'vote_counter',
      align: 'left',
    },
  ];
  //getter für projekte 
  get users() {
    return readAdminUsers(this.$store);
  }

  public async mounted() {
    await dispatchGetProjectData(this.$store);
  }
}
</script>