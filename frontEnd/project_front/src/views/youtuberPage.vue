<template>
  <div>
    <!-- header -->
    <v-card flat class="pa-0">
      <v-img :src="youtuber.bannerImageLink" class="py-6 lighten-5">
        <!-- <i class="font-weight-black display-4 jb">YOUTUBER</i> -->
      </v-img>
    </v-card>

    <!-- <v-card>
      <v-card-title class="justify-center py-6" style="background-color:#cdcdcd ; height : 300px">
        <i class="font-weight-black display-3" color="red">YOUTUBERPAGE</i>
      </v-card-title>
    </v-card>-->

    <!-- content -->
    <v-container>
      <!-- <v-card flat class="pa-0">
        <v-img :src="youtuber.bannerImageLink" class="py-6 lighten-5">
        </v-img>
      </v-card>-->
      <transition appear name="slide-fade">
        <!--기본정보-->
        <v-card class="my-3" outlined flat>
          <v-container fluid>
            <v-row>
              <!-- thumbnail -->
              <v-col cols="2" class="pa-3">
                <v-img class="circle" :src="youtuber.thumbnails" flat :aspect-ratio="1/1" />
              </v-col>

              <!-- 기본정보 -->
              <v-col cols="10">
                <v-row>
                  <v-col class="pb-0">
                    <p class="font-weight-black thin display-3 ma-0">{{youtuber.channelName}}</p>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="pt-0">
                    <span class="font-weight-light">개설일 : {{youtuber.publishedDate}} &nbsp;&nbsp;</span>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col class="pa-0">
                    <v-divider></v-divider>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col>
                    <span class="font-weight-bold">구독자 수</span>
                    <br />
                    {{youtuber.subscriber}}
                  </v-col>
                  <v-divider vertical class="mx-3"></v-divider>
                  <v-col>
                    <span class="font-weight-bold">총 영상 수</span>
                    <br />
                    {{youtuber.totalVideoCount}}
                  </v-col>
                  <v-divider vertical class="mx-3"></v-divider>
                  <v-col>
                    <span class="font-weight-bold">총 영상조회 수</span>
                    <br />
                    {{youtuber.totalViewCount}}
                  </v-col>
                  <v-spacer></v-spacer>
                </v-row>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </transition>

      <v-row>
        <v-col cols="9">
          <v-card outlined flat>
            <apexchart type="radar" height="350" :options="chartOptions" :series="series"></apexchart>
          </v-card>
        </v-col>
        <v-col cols="3">
          <v-card outlined flat>
            <v-avatar color="red">
              <span class="white--text headline">A</span>
            </v-avatar>
          </v-card>
        </v-col>
      </v-row>

      <!-- mainContainer -->
      {{this.$route.query.yno}}
      <v-divider></v-divider>
      {{youtuber.yno}}
      <br />
      {{youtuber.channelName}}
      <br />
      {{youtuber.youtuberName}}
      <br />
      {{youtuber.channelDescription}}
      <br />
      {{youtuber.namuwiki}}
      <br />
      {{youtuber.instagram}}
      <br />
      {{youtuber.facebook}}
      <br />
      {{youtuber.thumbnails}}
      <br />
      {{youtuber.publishedDate}}
      <br />
      {{youtuber.subscriber}}
      <br />
    </v-container>
  </div>
</template>

<script>
import {
  // mapState,
  mapGetters
} from "vuex";
import Constant from "../vuex/Constant";


export default {
  components: {
    
  },
  name: "youtuberPage",
  created() {
    console.log(this.$route.query);
    this.$vuetify.goTo(0);
    this.$store.dispatch(Constant.GET_YOUTUBER, {
      yno: this.$route.query.yno
    });
    console.log(this.$store.state.youtuber.yno);
  },
  methods: {},
  computed: {
    ...mapGetters({
      youtuber: "youtuber"
    })
  },
  data() {
    return {
       series: [{
            name: 'Series 1',
            data: [80, 50, 30, 40, 100, 20],
          }, {
            name: 'Series 2',
            data: [20, 30, 40, 80, 20, 80], 
          }, {
            name: 'Series 3',
            data: [44, 76, 78, 13, 43, 10],
          }],
          chartOptions: {
            chart: {
              height: 350,
              type: 'radar',
              dropShadow: {
                enabled: true,
                blur: 1,
                left: 1,
                top: 1
              }
            },
            title: {
            },
            stroke: {
              width: 0
            },
            fill: {
              opacity: 0.4
            },
            markers: {
              size: 0
            },
            xaxis: {
              categories: ['2011', '2012', '2013', '2014', '2015', '2016']
            }
          },
          
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
  color: red;
}
</style>
