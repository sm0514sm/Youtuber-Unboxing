<template>
  <div>
    <v-card>
      <v-card-title class="justify-center py-6" style="background-color:#cdcdcd ; height : 300px">
        <i class="font-weight-black display-3">MemberPage</i>
      </v-card-title>
    </v-card>
    <v-container name="container" background-color="transparent">
      
<template>
  <v-data-table
    :headers="headers"
    :items="fav"
    sort-by="calories"
    class="elevation-1"
  >
  
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-toolbar-title>즐겨찾기 목록</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
      </v-toolbar>
    </template>
    <template v-slot:item.action="{ item }">
      <v-icon
        small
        @click="deleteItem(item)"
      >
        delete
      </v-icon>
    </template>

    <template v-slot:item.thumbnails="{ item }">
                <v-card color="#00000000" flat :to="{ path: 'youtuberPage', query: { yno : item.yno}}">
                  <v-row>
                    <v-col cols="2" class = "px-0">
                      <v-card color="#00000000"   width="50px" flat>
                        <v-responsive :aspect-ratio="1/1">
                          <v-img class="circle" :src="item.thumbnails" flat/>
                        </v-responsive>
                      </v-card>

                    </v-col>
                    <v-col cols="10" class = "px-0">
                      <v-container fill-height>
                        <v-layout align-center>
                          <v-flex xs12 text-xs-center><div class="font-weight-light">{{item.channelName}}</div></v-flex>
                        </v-layout>
                      </v-container>
                    </v-col>
                  </v-row>
                </v-card>
              </template>


  </v-data-table>
</template>
    </v-container>
    
  </div>
</template>



<script>
import axios from "axios";
  export default {
    data: () => ({
      headers: [
        { text: '채널 이름', align:'left', value:'thumbnails', sortable:false},
        { text: '구독자', value: 'subscriber' },
        { text: '시청수', value: 'totalViewCount' },
        { text: '영상수', value: 'totalVideoCount' },
        { text: '등급', value: 'grade' },
        { text: '삭제', value: 'action', sortable: false },
      ],
      fav: [],
    }),
    created () {
      this.initialize()
    },

    methods: {
      initialize () {
        axios.get("http://localhost:8080/favorite/user/"+this.$session.get('token'))
        .then(response=>{
          console.log(response)
          this.fav = response.data.data
          console.log(this.fav)
        })
      },
      deleteItem (item) {
        const index = this.fav.indexOf(item)
        console.log(item.yno)
        if(confirm('Are you sure you want to delete this item?')){
          this.fav.splice(index, 1)
          let par = item.yno+"_"+this.$session.get('token')
      let deleteUrl = "http://localhost:8080/favorite/delete/"+par
      axios.delete(deleteUrl)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
        }
      },
      
    },
  }
</script>

<style scoped>
.jb {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.circle{
  border-radius: 50%;
}
</style>
