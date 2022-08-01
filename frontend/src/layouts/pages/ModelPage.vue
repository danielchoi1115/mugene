<template>
  <div class="grid justify-center gap-6 mt-10 grid-cols-3">
    <div
      class="w-full flex-row items-center p-4 bg-white rounded-lg shadow-xs dark:bg-gray-800 transition-height ease-in-out duration-300 {firstbox_height}"
    >
      <div>
        <div class="text-base text-left text-purple-700 dark:text-purple-200">
          <input
            id="report-name-inputbox"
            type="text"
            placeholder="Untitled"
            class="py-1 px-3 rounded-lg outline-none font-semibold text-black placeholder:text-gray-500 transition-width duration-100 ease-in-out dark:bg-gray-800 hover:bg-purple-100 focus:bg-purple-200 dark:hover:bg-gray-600 dark:focus:bg-gray-600 dark:bg-opacity-80 dark:text-purple-100 dark:placeholder:text-gray-400"
            style="width: {titleWidth}; min-width: 5.6rem; max-width: 100%"
            bind:value="{reportName}"
            on:blur="{calTitleWidth}"
          />
          <div class="mt-1">
            <!-- <input type="text" value="" placeholder="#hashtags" /> -->
            <!-- <HashtagTyper bind:hashtags /> -->
          </div>
        </div>
      </div>
      <div class="flex my-3">
        <svg width="600" height="1" viewBox="0 0 400 1" fill="none" xmlns="http://www.w3.org/2000/svg" class="mx-auto">
          <line x1="0.0383301" y1="0.75" x2="400" y2="0.75" stroke="#545454" stroke-width="0.5" />
        </svg>
      </div>
      <div class="flex-row bg-white rounded-lg shadow-xs p-3 dark:bg-gray-800">
        <div class="inline-flex flex">
          Radiobox1
          <!-- <Radiobox
          text={"Sequence Selection"}
          value={"select_sequence"}
          bind:group={sequenceOption}
        /> -->
        </div>
        <div class="inline-flex flex">
          Radiobox2
          <!-- <Radiobox
          text={"or input own Sequence"}
          value={"own_sequence"}
          bind:group={sequenceOption}
        /> -->
        </div>
      </div>
      <!-- {#if sequenceOption === "select_sequence"}
      <div
        class="mt-2 transition-all duration-300"
        in:scale={{ duration: 200, delay: 200, easing: expoOut }}
        out:scale={{ duration: 200, easing: expoIn }}
      >
        <Searchbar bind:selectedSeqences />
      </div>
    {:else if sequenceOption === "own_sequence"}
      <div
        class="transition-all duration-300"
        in:scale={{ duration: 200, delay: 200, easing: expoOut }}
        out:scale={{ duration: 200, easing: expoIn }}
      >
        <SequenceTyper
          bind:selectedSeqences
          bind:selectedRegion={seqTyper_selectedRegion}
          bind:sequenceInput={seqTyper_sequenceInput}
          bind:text={seqTyper_text}
        />
      </div>
    {/if}
    {#if selectedSeqences.length > 0}
      <div class="my-2 flex">
        <p
          class="pl-2 text-sm text-left text-gray-700 font-semibold dark:text-gray-200 mb-1 mt-4"
        >
          Selected Sequences
        </p>
      </div>
    {/if}
    <div class="grid grid-cols-2 flex-row flex-col gap-2">
    {#each selectedSeqences as sequence (sequence.sequenceId)}
      <div
        class="p-1 flex inline-flex"
        in:scale={{ duration: 200, easing: expoOut }}
        out:scale={{ duration: 200, easing: expoIn }}
        animate:flip={{ duration: 200 }}
      >
        <Chips
          text={sequence.filename}
          removable
          on:close={() => removeSelection(sequence.sequenceId)}
        />
      </div>
    {/each}
    </div>
  </div>
  {#if selectedSeqences.length != 0 || savedParameters.length != 0}
    <div class="flex-row items-center w-full" transition:fly={transition}>
      <OptionBox
        bind:options
        bind:isInputValid
        bind:mhc
        on:click={() => addParameterSelection()}
      />
    </div>
  {/if}
  {#if savedParameters.length > 0}
    Saved Parameters
    <div class="flex-row  items-center w-full" transition:fly={transition}>
      <div
        class="w-full flex-row h-9/10 items-center p-4 bg-white rounded-lg shadow-xs dark:bg-gray-800 "
      >
        <div>
          <p
            class="pl-2 text-md text-center font-semibold text-purple-700 dark:text-purple-200"
          >
            Saved Parameters
          </p>
        </div>
        <div class="flex my-3">
          <svg
            width="400"
            height="1"
            viewBox="0 0 400 1"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            class="mx-auto"
          >
            <line
              x1="0.0383301"
              y1="0.75"
              x2="400"
              y2="0.75"
              stroke="#545454"
              stroke-width="0.5"
            />
          </svg>
        </div>
        <div
          class="w-full mt-4 rounded-lg shadow-xs"
          style="overflow-y: scroll;
          overflow-y: overlay; -ms-overflow-style: none; max-height: 27rem"
        >
          <div class="w-full overflow-y-hidden">
            <table id="saved-parameter-container" class="w-full wrap">
              <thead>
                <tr
                  class="text-xs font-semibold tracking-wide text-left text-gray-500 uppercase border-b dark:border-gray-700 bg-gray-50 dark:text-gray-400 dark:bg-gray-800"
                >
                  <th class="px-1 py-3" />
                  <th class="px-4 py-3">Sequence</th>
                  <th class="px-4 py-3">Saved Time</th>
                </tr>
              </thead>
              <tbody class="divide-y dark:divide-gray-700 ">
                {#each savedParameters as { id, sequences, savedTime } (id)}
                  <tr
                    class=" text-gray-700 dark:text-gray-400 bg-white dark:bg-gray-800"
                    animate:flip={{ duration: 300 }}
                    in:fly={{
                      duration: 300,
                      y: -5,
                      easing: sineIn,
                    }}
                    out:scale={{
                      duration: 300,
                      easing: sineOut,
                    }}
                  >
                    <SavedParameter
                      {id}
                      {sequences}
                      parameter-saved-time={savedTime}
                      on:remove={() => deleteSavedParameters(id)}
                    />
                  </tr>
                {/each}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      {#if savedParameters.length > 0}
        <div transition:fade={{ duration: 200 }}>
          <AddButton on:click={() => runPrediction()} value="Run Prediction" />
        </div>
      {/if}
    </div>
  {/if} -->
    </div>
  </div>
</template>
