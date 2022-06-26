<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title> Schulen verwalten</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color='primary' to='/account/main/admin/CreateSchool'
        >Create School</v-btn
      >
    </v-toolbar>
    <v-data-table :headers='headers' :items='users'>
      <template slot='items' slot-scope='props'>
        <td>{{ props.item.school_name }}</td>
        <td>{{ props.item.school_id }}</td>
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
import { dispatchGetSchools } from '@/store/admin/actions';

@Component
export default class AdminUsers extends Vue {
  public headers = [
    {
      text: 'Name',
      sortable: true,
      value: 'school_name',
      align: 'left',
    },
    {
      text: 'ID',
      sortable: true,
      value: 'school_id',
      align: 'left',
    },
    
  ];
  /*
  get schools(context: MainContext) {
      return users();
  }

  get users(token: string) {
    return await schools(this.$store);
  }
  */
  get users() {
    return readAdminUsers(this.$store);
  }
  
  public async mounted() {
    await dispatchGetSchools(this.$store);
  }
}
</script>