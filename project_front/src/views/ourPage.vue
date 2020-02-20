<template>
  <div>
    <v-card>
      <v-card-title class="justify-center py-6" style="background-color:#6688ff ; height : 300px">
        <v-icon size="70" class="mr-2" color="white">mdi-account-group</v-icon>
        <span style="text-shadow: 0 0 2px #000;font-size: 2.5em;color:white">ABOUT US</span>
      </v-card-title>
    </v-card>
    <v-container class="pa-0">
      <!--기본정보-->
      <div v-for="(cardinfo, index) in dummyData" :key="index">
        <v-card class="my-3" outlined flat>
          <v-container fluid>
            <v-row>
              <!-- thumbnail -->
              <v-col cols="2" class="pa-3">
                <v-img
                  class="circle"
                  :src="require('@/assets/' + cardinfo.image + '.png')"
                  flat
                  :aspect-ratio="1 / 1"
                />
              </v-col>

              <!-- 기본정보 -->
              <v-col cols="10">
                <v-row>
                  <v-col class="pb-0">
                    <span class="font-weight-black thin display-3 ma-0">
                      {{
                      cardinfo.name
                      }}
                    </span>
                    <v-btn rounded color="#6688ff" justify="center" class="ml-2" dark>
                      <b>{{ cardinfo.position }}</b>
                    </v-btn>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="ml-1 pt-0 pl-5">
                    <span class="font-weight-light mr-4">{{ cardinfo.birth }}</span>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="ma-0 pa-0">
                    <v-divider class="pa-0 ma-0"></v-divider>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col>
                    <span class="font-weight-bold">STACK</span>
                    <div v-for="stack in cardinfo.stacks" :key="stack">
                      <v-row align="center" style="float: left;">
                        <v-img
                          width="50px"
                          class="ml-2 mr-7 my-3"
                          :src="require('@/assets/' + stack + '.png')"
                        />
                      </v-row>
                    </div>
                  </v-col>
                  <v-divider vertical class="mx-3"></v-divider>
                  <v-col>
                    <span class="font-weight-bold">POSITION</span>
                    <br />
                    <div v-for="feat in cardinfo.feat" :key="feat">{{ feat }}</div>
                  </v-col>
                  <v-divider vertical class="mx-3"></v-divider>
                  <!-- 외부링크 -->
                  <v-col cols="4">
                    <v-row align="center" style="float: left;">
                      <!--youtuber -->
                      <v-img
                        v-if="cardinfo.git"
                        width="32px"
                        class="ml-2 mr-2 my-3"
                        src="../assets/githubIcon.png"
                        style="cursor:pointer"
                        @click="gitLink(cardinfo.git)"
                      />
                      <v-img
                        v-if="cardinfo.insta"
                        width="32px"
                        class="ml-2 mr-2 my-3"
                        src="../assets/instagramIcon.png"
                        @click="instaLink(cardinfo.insta)"
                        style="cursor:pointer"
                      />
                      <v-img
                        v-if="cardinfo.youtube"
                        width="32px"
                        class="ml-2 mr-2 my-3"
                        src="../assets/youtubeIcon.png"
                        @click="youLink(cardinfo.youtube)"
                        style="cursor:pointer"
                      />
                      <v-img
                        v-if="cardinfo.tistory"
                        width="40px"
                        class="ml-2 mr-2 my-3"
                        src="../assets/tistoryIcon.png"
                        @click="tiLink(cardinfo.tistory)"
                        style="cursor:pointer"
                      />
                      <v-img
                        v-if="cardinfo.blog"
                        width="50px"
                        class="ml-2 mr-2 my-3"
                        src="../assets/blogIcon.png"
                        @click="blogLink(cardinfo.blog)"
                        style="cursor:pointer"
                      />
                    </v-row>
                  </v-col>
                  <v-spacer></v-spacer>
                </v-row>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </div>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "ourPage",
  components: {},
  beforecreated() {},
  created() {},
  mounted() {
    this.$vuetify.goTo(0);
  },
  methods: {
    blogLink(link) {
      window.open(link);
    },
    tiLink(link) {
      var ti = "https://" + link + ".tistory.com/";
      window.open(ti);
    },
    gitLink(link) {
      var git = "https://github.com/" + link;
      window.open(git);
    },
    instaLink(link) {
      var insta = "https://www.instagram.com/" + link;
      window.open(insta);
    },
    youLink(link) {
      var you = "https://www.youtube.com/" + link;
      window.open(you);
    }
  },
  computed: {},
  data() {
    return {
      dummyData: [
        {
          name: "김주희",
          position: "BACK / DESIGN",
          image: "KJH",
          birth: "yylcd99999@gmail.com",
          git: "juheekimm",
          // gitlab: "juheekim",
          // insta: "sally_0607",
          tistory: "buddev",
          stacks: ["spring", "mariadb"],
          feat: ["SPRING", "DATABASE", "CSS"]
        },
        {
          name: "김태민",
          position: "Front End",
          image: "KTM",
          birth: "taeminkim23@gmail.com",
          git: "taemtaemKim",
          // gitlab: "taemin",
          insta: "merona_mango",
          stacks: ["vue", "vuetify"],
          feat: ["VUE MASTER"]
        },
        {
          name: "박진홍",
          position: "Data Collect",
          image: "PJH",
          birth: "mpcato37@gmail.com",
          git: "porciuscato",
          // gitlab: "mpcato",
          insta: "__jin__hong__",
          blog: "https://porciuscato.github.io/",
          stacks: ["aws", "django"],
          feat: ["YOUTUBE API", "SERVER AUTOMATION"]
        },
        {
          name: "이상민",
          position: "Data / Server",
          image: "LSM",
          birth: "sm0514sm@gmail.com",
          git: "sm0514sm",
          // gitlab: "lifaon",
          insta: "lifaon_sm",
          youtube: "channel/UC5cGDQN2ZYw4GAZGUIkwjcw",
          tistory: "lifaon",
          stacks: ["aws", "django"],
          feat: ["YOUTUBE API", "GIT MASTER", "AWS"]
        },
        {
          name: "홍기환",
          position: "Back / Front",
          image: "HKH",
          birth: "airaider77@gmail.com",
          git: "airaider",
          // gitlab: "airaider",
          insta: "hongki772",
          stacks: ["spring", "vue"],
          feat: ["TEAM LEADER", "LOGIN", "VUE"]
        }
      ]
    };
  }
};
</script>

<style scoped>
.slide-fade-enter-active {
  transition: all 2s ease;
}
.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(100px);
  opacity: 0;
}
.circle {
  border-radius: 50%;
}
.jb {
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 3s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
.ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3; /* number of lines to show */
}
</style>
