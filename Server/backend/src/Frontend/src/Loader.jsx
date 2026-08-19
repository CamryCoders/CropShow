
function Loader(){

    return(
        
<div class="h-full w-full flex flex-col items-center justify-center p-6 bg-emerald-50/50 rounded-xl border border-dashed border-emerald-300">
    
    <div class="relative flex items-center justify-center mb-3">
        
        <div class="w-12 h-12 border-4 border-emerald-200 border-t-emerald-700 rounded-full animate-spin"></div>
        
        <i data-lucide="sprout" class="w-5 h-5 text-emerald-700 absolute"></i>
    </div>

   
    <p class="text-sm font-bold text-emerald-800 animate-pulse tracking-wide">
        Running Crop Recommendation Model...
    </p>
    <p class="text-xs text-slate-500 mt-1">
        Evaluating N-P-K levels, pH, and climate conditions
    </p>
</div>
    )
}

export {Loader}