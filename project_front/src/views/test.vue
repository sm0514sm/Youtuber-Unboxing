<template>
    <div class="demo-height-root" @click="triggerAction">
        <animation-css
            :animation-type="AnimationType.TADA"
            v-model="trigger">
            <p class="animated-body">案例库抵押后泵</p>
        </animation-css>
    </div>
</template>


<script>
    // Load on demand
    import {AnimationCss, AnimationCssType} from 'vue-animation'

    export default {
        components: {
            [AnimationCss.name]: AnimationCss,
        },
        data () {
            return {
                AnimationType: AnimationCssType,
                trigger: false
            };
        },
        methods: {
            triggerAction() {
                this.trigger = true;
            }
        }
    }
</script>