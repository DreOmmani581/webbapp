<template>
  <v-content>
   <v-toolbar >
     <img width="200" height="44" src="https://wirfuerschule.de/wp-content/uploads/2020/05/wirfu%CC%88rschule_logo-1024x226.png">
              <v-toolbar-title>
              
        
              {{"Homepage"}}</v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>
    <v-container fluid fill-height>
      <v-layout align-left justify-left>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-12">
            <v-toolbar dark color="teal accent-3">
              <v-toolbar-title>{{"Projektabgabe"}}</v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>
            <v-card-text>
            <v-flex><router-link to="/account">zum Login</router-link></v-flex>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>
export default {
    name: 'home',
};
</script>

<style>
.v-toolbar__content{
      background-image: linear-gradient(160deg, #5AC6CE 0%, #28FFCF 73%);

}
</style>