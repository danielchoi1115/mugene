<template>
  <header class="z-0 py-4 bg-white dark:bg-gray-800 rounded-t-2xl">
    <div class="container flex items-center justify-between h-full px-6 mx-auto text-purple-600 dark:text-purple-300">
      <a class="justify-center flex mx-auto pl-10 text-lg font-bold text-gray-800 dark:text-gray-200" href="#">
        MuGene
      </a>

      <ul class="flex items-center flex-shrink-0 space-x-6">
        <!-- Theme toggler -->
        <li class="flex">
          <ThemeToggler></ThemeToggler>
        </li>
        <!-- Notifications menu -->
        <li v-click-outside="console.log('noti menu closed')" class="relative">
          <button
            class="relative align-middle rounded-md focus:outline-none focus:shadow-outline-purple"
            aria-label="Notifications"
            aria-haspopup="true"
            @click="console.log('open noti menu')"
          >
            <svg class="w-5 h-5" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20">
              <path
                d="M10 2a6 6 0 00-6 6v3.586l-.707.707A1 1 0 004 14h12a1 1 0 00.707-1.707L16 11.586V8a6 6 0 00-6-6zM10 18a3 3 0 01-3-3h6a3 3 0 01-3 3z"
              />
            </svg>
            <!-- Notification badge -->
            <span
              aria-hidden="true"
              class="absolute top-0 right-0 inline-block w-3 h-3 transform translate-x-1 -translate-y-1 bg-red-600 border-2 border-white rounded-full dark:border-gray-800"
            />
          </button>

          <!-- <NotificationMenu /> -->
        </li>
        <!-- Profile menu -->
        <li v-click-outside="console.log('profileMenu closed')" class="relative">
          <button
            class="align-middle rounded-full focus:shadow-outline-purple focus:outline-none"
            aria-label="Account"
            aria-haspopup="true"
            @click="console.log('profile menu clicked')"
          >
            <img
              class="object-cover w-8 h-8 rounded-full"
              src="https://images.unsplash.com/photo-1502378735452-bc7d86632805?ixlib=rb-0.3.5&amp;q=80&amp;fm=jpg&amp;crop=entropy&amp;cs=tinysrgb&amp;w=200&amp;fit=max&amp;s=aa3a807e1bbdfd4364d1f449eaa96d82"
              alt=""
              aria-hidden="true"
            />
          </button>
          <!-- <ProfileMenu /> -->
        </li>
      </ul>
    </div>
  </header>
</template>

<script>
import ThemeToggler from '../components/ThemeToggler.vue'
import ClickOutside from 'vue-click-outside'
export default {
  directives: {
    ClickOutside,
  },
  components: { ThemeToggler },
}
</script>
