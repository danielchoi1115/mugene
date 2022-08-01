<template>
  <aside
    class="z-0 w-64 overflow-y-auto bg-white dark:bg-gray-800 md:block flex-shrink-0 rounded-tl-2xl rounded-bl-2xl"
  >
    <div class="py-4 pt-20 text-gray-500 dark:text-gray-400">
      <a class="ml-20 text-lg font-bold text-gray-800 dark:text-gray-200" href="#" />
      <ul class="mt-6">
        <li class="relative px-6 pb-5 mb-5 shadow-md">
          <a
            class="inline-flex items-center w-full text-md font-semibold text-gray-800 transition-colors duration-150 hover:text-gray-800 dark:hover:text-gray-200 dark:text-gray-100"
            href="index.html"
          >
            <span class="ml-4 mr-16">Cancer: LUAD</span>
            <svg class="w-4 h-4" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20">
              <path
                fill-rule="evenodd"
                d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                clip-rule="evenodd"
              /></svg
          ></a>
        </li>
      </ul>
      <ul>
        <li class="relative px-6 py-3">
          <a
            class="flex-row items-center w-full text-purple-500 duration-150 hover:text-purple-800 dark:hover:text-purple-200"
            href="forms.html"
          >
            <span class="flex ml-4 text-sm font-semibold mb-4">Saved Results</span>
            <span class="flex ml-12 mb-3 text-sm font-medium text-gray-500"
              ><svg
                class="w-5 h-5 mr-3"
                aria-hidden="true"
                fill="none"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"
                /></svg
              >2022 Feb</span
            ><span class="flex ml-12 mb-3 text-sm font-medium text-gray-500"
              ><svg
                class="w-5 h-5 mr-3"
                aria-hidden="true"
                fill="none"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"
                /></svg
              >2022 Jan</span
            ><span class="flex ml-12 mb-3 text-sm font-medium text-gray-500"
              ><svg
                class="w-5 h-5 mr-3"
                aria-hidden="true"
                fill="none"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"
                /></svg
              >2021 Dec</span
            >
          </a>
        </li>
        <li class="relative px-6 py-3">
          <a
            class="inline-flex items-center w-full text-sm font-semibold transition-colors duration-150 hover:text-gray-800 dark:hover:text-gray-200"
            href="cards.html"
          >
            <span class="ml-4">Shared With Me</span>
          </a>
        </li>
        <li class="relative px-6 py-3">
          <a
            class="inline-flex items-center w-full text-sm font-semibold transition-colors duration-150 hover:text-gray-800 dark:hover:text-gray-200"
            href="charts.html"
          >
            <span class="ml-4">Recents</span>
          </a>
        </li>
        <li class="relative px-6 py-3">
          <a
            class="inline-flex items-center w-full text-sm font-semibold transition-colors duration-150 hover:text-gray-800 dark:hover:text-gray-200"
            href="buttons.html"
          >
            <span class="ml-4">#Hashtags</span>
          </a>
        </li>
        <li class="relative px-6 py-3">
          <a
            class="inline-flex items-center w-full text-sm font-semibold transition-colors duration-150 hover:text-gray-800 dark:hover:text-gray-200"
            href="modals.html"
          >
            <span class="ml-4">Trash</span>
          </a>
        </li>
      </ul>
      <div class="px-6 my-6">
        <button
          class="flex items-center justify-between w-full px-4 py-2 text-sm font-medium leading-5 text-white transition-colors duration-150 bg-purple-600 border border-transparent rounded-lg active:bg-purple-600 hover:bg-purple-700 focus:outline-none focus:shadow-outline-purple"
        >
          Create New
          <span class="w-5 h-5 bg-purple-300 rounded-md" aria-hidden="true">+</span>
        </button>
      </div>
    </div>
  </aside>
</template>
