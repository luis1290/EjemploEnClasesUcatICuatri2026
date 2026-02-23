<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;


/*
|--------------------------------------------------------------------------
| Ruta de prueba
|--------------------------------------------------------------------------
*/

Route::get('/ping', function () {
    return response()->json([
        'message' => 'API funcionando correctamente'
    ]);
});


