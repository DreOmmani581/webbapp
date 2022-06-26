<template>
  <v-content>
    <v-box>
      <img
        width='200'
        height='44'
        src='https://wirfuerschule.de/wp-content/uploads/2020/05/wirfu%CC%88rschule_logo-1024x226.png'
      />

      <v-spacer></v-spacer>
    </v-box>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class='elevation-12'>
            <v-toolbar dark color='teal accent-3'>
              <v-toolbar-title>{{
                'Bewertungslink erstellen'
              }}</v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>
            <v-card-text>
              <select name='Klassen' id='Klassen'>
                <option value='4a'>Klasse 4a</option>
                <option value='3b'>Klasse 3b</option>
              </select>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn @click.prevent='submit'>Generieren</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>


<script lang='ts'>
import { component } from 'vue/types/umd';
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class VotingLinkCreator extends Vue {}
</script>

<style>
.v-toolbar__content {
  background-image: linear-gradient(160deg, #5ac6ce 0%, #28ffcf 73%);
}
#Klassen {
  border: 1px solid black;
  box-shadow: 10px 5px 5px black;
}
</style>